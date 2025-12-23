# app/main.py
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
import uuid
import uvicorn

from app.database import engine, Base, get_db
from app.services.test_service import TestService
from app.services.calculation_service import CalculationService
from app.models import TestResult
from app.auth.models import User
from app.auth.routes import auth_router
from app.auth.dependencies import get_current_user

# Инициализация сервисов
test_service = TestService()
calculation_service = CalculationService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Создание БД при запуске"""
    print("Создание таблиц БД...")
    Base.metadata.create_all(bind=engine)

    print("Загрузка тестовых данных...")
    yield

    print("Приложение завершает работу...")


app = FastAPI(
    title="Psychology Tests",
    description="Веб-сервис для психологических тестов",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Шаблоны
templates = Jinja2Templates(directory="app/templates")

# Подключаем роутер авторизации
app.include_router(auth_router)


# ================ API ЭНДПОИНТЫ ================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, current_user: User = Depends(get_current_user)):
    """Главная страница с тестами"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "current_user": current_user
    })


@app.get("/api/tests", response_class=JSONResponse)
async def get_all_tests():
    """Получить список всех доступных тестов"""
    tests = test_service.get_available_tests()
    return {"tests": tests}


@app.get("/api/tests/{test_code}", response_class=JSONResponse)
async def get_test(test_code: str):
    """Получить конкретный тест с вопросами"""
    test = test_service.get_test_by_code(test_code)
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    return test


@app.post("/api/tests/{test_code}/submit", response_class=JSONResponse)
async def submit_test(
        test_code: str,
        request: Request,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    """Отправить ответы на тест и получить результаты"""
    try:
        data = await request.json()
        answers_data = data.get("answers", [])

        # Получаем тест
        test = test_service.get_test_by_code(test_code)
        if not test:
            raise HTTPException(status_code=404, detail="Тест не найден")

        # Преобразуем ответы для расчета
        answers = []
        for answer in answers_data:
            question_id = answer.get("question_id")
            selected_option_id = answer.get("selected_option_id")

            # Находим вопрос и выбранный вариант
            for question in test["questions"]:
                if question["id"] == question_id:
                    for option in question["options"]:
                        if option["id"] == selected_option_id:
                            answers.append({
                                "question_id": question_id,
                                "selected_option_id": selected_option_id,
                                "value": option["value"]
                            })
                            break
                    break

        # Рассчитываем результаты
        result = calculation_service.calculate_results(test_code, answers)

        # Генерируем сессию для анонимного пользователя
        session_id = str(uuid.uuid4())

        # Сохраняем результат в БД, если пользователь авторизован
        if current_user:
            test_result = TestResult(
                test_code=test_code,
                test_name=test["name"],
                total_score=result.get("total_score", 0),
                answers=answers_data,
                interpretation=result.get("interpretation", ""),
                recommendations=", ".join(result.get("recommendations", [])),
                session_id=session_id,
                user_id=current_user.id
            )

            db.add(test_result)
            db.commit()

        return {
            "success": True,
            "test_name": test["name"],
            "result": result,
            "session_id": session_id,
            "user_id": current_user.id if current_user else None
        }

    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"success": False, "error": str(e)}
        )


@app.get("/api/user/stats", response_class=JSONResponse)
async def get_user_stats(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    """Получить статистику пользователя"""
    if not current_user:
        raise HTTPException(status_code=401, detail="Требуется авторизация")

    # Подсчет пройденных тестов
    tests_count = db.query(TestResult).filter(
        TestResult.user_id == current_user.id
    ).count()

    # Получение последней активности
    last_test = db.query(TestResult).filter(
        TestResult.user_id == current_user.id
    ).order_by(TestResult.created_at.desc()).first()

    return {
        "tests_count": tests_count,
        "last_activity": last_test.created_at.strftime("%d.%m.%Y") if last_test else "Нет данных"
    }


@app.get("/api/user/tests", response_class=JSONResponse)
async def get_user_tests(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    """Получить историю тестов пользователя"""
    if not current_user:
        raise HTTPException(status_code=401, detail="Требуется авторизация")

    tests = db.query(TestResult).filter(
        TestResult.user_id == current_user.id
    ).order_by(TestResult.created_at.desc()).limit(20).all()

    return [
        {
            "id": test.id,
            "test_name": test.test_name,
            "test_code": test.test_code,
            "total_score": test.total_score,
            "created_at": test.created_at.isoformat(),
            "interpretation": test.interpretation
        }
        for test in tests
    ]


@app.get("/health", response_class=JSONResponse)
async def health_check():
    """Проверка работоспособности API"""
    return {"status": "healthy", "service": "Psychology Tests"}


# ================ HTML СТРАНИЦЫ ================

@app.get("/test/{test_code}", response_class=HTMLResponse)
async def test_page(
        request: Request,
        test_code: str,
        current_user: User = Depends(get_current_user)
):
    """Страница прохождения теста"""
    test = test_service.get_test_by_code(test_code)
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")

    return templates.TemplateResponse("test.html", {
        "request": request,
        "test": test,
        "current_user": current_user
    })


@app.get("/result", response_class=HTMLResponse)
async def result_page(
        request: Request,
        current_user: User = Depends(get_current_user)
):
    """Страница с результатами"""
    return templates.TemplateResponse("result.html", {
        "request": request,
        "current_user": current_user
    })


# Обработчик 404 для SPA
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: Exception):
    if request.url.path.startswith("/api/"):
        return JSONResponse(
            status_code=404,
            content={"detail": "Ресурс не найден"}
        )

    current_user = await get_current_user(request, get_db())
    return templates.TemplateResponse("index.html", {
        "request": request,
        "current_user": current_user
    })


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )