from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from contextlib import asynccontextmanager
import uuid
import uvicorn

from app.database import engine, Base
from app.services.test_service import TestService
from app.services.calculation_service import CalculationService
from app.models import TestResult

# Инициализация сервисов
test_service = TestService()
calculation_service = CalculationService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Создание БД при запуске"""
    print("Создание таблиц БД...")
    Base.metadata.create_all(bind=engine)

    print("Загрузка тестовых данных...")
    # Тесты уже загружены при инициализации TestService

    yield

    print("Приложение завершает работу...")


app = FastAPI(
    title="Psychology Tests",
    description="Веб-сервис для психологических тестов",
    version="1.0.0",
    lifespan=lifespan
)

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Шаблоны
templates = Jinja2Templates(directory="app/templates")


# ================ API ЭНДПОИНТЫ ================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Главная страница с тестами"""
    return templates.TemplateResponse("index.html", {"request": request})


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
async def submit_test(test_code: str, request: Request):
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


        return {
            "success": True,
            "test_name": test["name"],
            "result": result,
            "session_id": session_id
        }

    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"success": False, "error": str(e)}
        )


@app.get("/health", response_class=JSONResponse)
async def health_check():
    """Проверка работоспособности API"""
    return {"status": "healthy", "service": "Psychology Tests"}


# ================ HTML СТРАНИЦЫ ================

@app.get("/test/{test_code}", response_class=HTMLResponse)
async def test_page(request: Request, test_code: str):
    """Страница прохождения теста"""
    test = test_service.get_test_by_code(test_code)
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")

    return templates.TemplateResponse("test.html", {
        "request": request,
        "test": test
    })


@app.get("/result", response_class=HTMLResponse)
async def result_page(request: Request):
    """Страница с результатами"""
    return templates.TemplateResponse("result.html", {"request": request})


# Обработчик 404 для SPA
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: Exception):
    if request.url.path.startswith("/api/"):
        return JSONResponse(
            status_code=404,
            content={"detail": "Ресурс не найден"}
        )
    return templates.TemplateResponse("index.html", {"request": request})




if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )