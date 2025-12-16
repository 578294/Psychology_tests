import json
from typing import List, Dict, Any, Optional

from app.tests import (
    BDITest, SuicideRiskTest, MBITest,
    SF36Test, IESRTest, SpielbergerTest
)

class TestService:
    """Сервис для работы с тестами"""

    def __init__(self):
        self.tests = {}
        self.test_classes = {}
        self.load_all_tests()

    def load_all_tests(self):
        """Загрузить все доступные тесты"""
        # Инициализация классов тестов
        self.test_classes = {
            "bdi_ii": BDITest(),
            "suicide_risk": SuicideRiskTest(),
            "mbi": MBITest(),
            "sf_36": SF36Test(),
            "ies_r": IESRTest(),
            "spielberger": SpielbergerTest()
        }

        # Загрузка данных тестов
        for code, test_instance in self.test_classes.items():
            self.tests[code] = test_instance.get_test_data()

    def get_available_tests(self) -> List[Dict[str, Any]]:
        """Получить список доступных тестов (без вопросов)"""
        result = []
        for code, test_data in self.tests.items():
            result.append({
                "id": code,
                "code": code,
                "name": test_data["name"],
                "description": test_data["description"],
                "questions_count": test_data["questions_count"],
                "time_limit": test_data.get("time_limit"),
                "min_score": test_data.get("min_score", 0),
                "max_score": test_data["max_score"]
            })
        return result

    def get_test_by_code(self, test_code: str) -> Optional[Dict[str, Any]]:
        """Получить тест по коду со всеми вопросами"""
        if test_code not in self.tests:
            return None

        return self.tests[test_code]

    def calculate_test_results(self, test_code: str, answers: List[Dict]) -> Dict[str, Any]:
        """Рассчитать результаты теста"""
        if test_code not in self.test_classes:
            raise ValueError(f"Тест {test_code} не найден")

        test_instance = self.test_classes[test_code]
        return test_instance.calculate(answers)