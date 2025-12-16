from typing import List, Dict, Any
from app.services.test_service import TestService


class CalculationService:
    """Сервис для расчета результатов тестов"""

    def __init__(self):
        self.test_service = TestService()

    def calculate_results(self, test_code: str, answers: List[Dict]) -> Dict[str, Any]:
        """Рассчитать результаты теста на основе кода теста"""
        return self.test_service.calculate_test_results(test_code, answers)