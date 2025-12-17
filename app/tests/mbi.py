"""
MBI (Maslach Burnout Inventory) - Опросник выгорания
22 вопроса, диапазон баллов: 0-132
"""


class MBITest:
    """Класс для работы с тестом MBI"""

    def __init__(self):
        self.code = "mbi"
        self.name = "Опросник выгорания MBI (Maslach Burnout Inventory)"
        self.description = "Диагностика профессионального выгорания по трем субшкалам: эмоциональное истощение, деперсонализация, редукция достижений"
        self.instructions = "Оцените, насколько часто вы испытываете следующие чувства, связанные с вашей работой."
        self.questions_count = 22
        self.min_score = 0
        self.max_score = 132
        self.time_limit = 12  # минут

    def get_test_data(self) -> dict:
        """Получить данные теста"""
        return {
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "instructions": self.instructions,
            "questions_count": self.questions_count,
            "min_score": self.min_score,
            "max_score": self.max_score,
            "time_limit": self.time_limit,
            "questions": self._get_questions()
        }

    def _get_questions(self) -> list:
        """Получить вопросы теста"""
        return [
            {
                "id": 1,
                "question_number": 1,
                "text": "Я чувствую себя эмоционально опустошенным из-за своей работы",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 1, "text": "Никогда", "value": 0},
                    {"id": 2, "text": "Очень редко", "value": 1},
                    {"id": 3, "text": "Иногда", "value": 2},
                    {"id": 4, "text": "Часто", "value": 3},
                    {"id": 5, "text": "Очень часто", "value": 4},
                    {"id": 6, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 2,
                "question_number": 2,
                "text": "К концу рабочего дня я чувствую себя как 'выжатый лимон'",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 7, "text": "Никогда", "value": 0},
                    {"id": 8, "text": "Очень редко", "value": 1},
                    {"id": 9, "text": "Иногда", "value": 2},
                    {"id": 10, "text": "Часто", "value": 3},
                    {"id": 11, "text": "Очень часто", "value": 4},
                    {"id": 12, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 3,
                "question_number": 3,
                "text": "Я чувствую усталость, когда утром встаю и думаю о предстоящем рабочем дне",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 13, "text": "Никогда", "value": 0},
                    {"id": 14, "text": "Очень редко", "value": 1},
                    {"id": 15, "text": "Иногда", "value": 2},
                    {"id": 16, "text": "Часто", "value": 3},
                    {"id": 17, "text": "Очень часто", "value": 4},
                    {"id": 18, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 4,
                "question_number": 4,
                "text": "Я легко понимаю, что чувствуют мои подопечные (клиенты, пациенты, ученики)",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 19, "text": "Всегда", "value": 5},
                    {"id": 20, "text": "Очень часто", "value": 4},
                    {"id": 21, "text": "Часто", "value": 3},
                    {"id": 22, "text": "Иногда", "value": 2},
                    {"id": 23, "text": "Очень редко", "value": 1},
                    {"id": 24, "text": "Никогда", "value": 0}
                ]
            },
            {
                "id": 5,
                "question_number": 5,
                "text": "Я чувствую, что работаю с некоторыми подопечными (клиентами, пациентами, учениками) как с бездушными предметами",
                "subscale": "Деперсонализация",
                "options": [
                    {"id": 25, "text": "Никогда", "value": 0},
                    {"id": 26, "text": "Очень редко", "value": 1},
                    {"id": 27, "text": "Иногда", "value": 2},
                    {"id": 28, "text": "Часто", "value": 3},
                    {"id": 29, "text": "Очень часто", "value": 4},
                    {"id": 30, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 6,
                "question_number": 6,
                "text": "Работа с людьми весь день требует большого напряжения",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 31, "text": "Никогда", "value": 0},
                    {"id": 32, "text": "Очень редко", "value": 1},
                    {"id": 33, "text": "Иногда", "value": 2},
                    {"id": 34, "text": "Часто", "value": 3},
                    {"id": 35, "text": "Очень часто", "value": 4},
                    {"id": 36, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 7,
                "question_number": 7,
                "text": "Я успешно решаю проблемы своих подопечных (клиентов, пациентов, учеников)",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 37, "text": "Всегда", "value": 5},
                    {"id": 38, "text": "Очень часто", "value": 4},
                    {"id": 39, "text": "Часто", "value": 3},
                    {"id": 40, "text": "Иногда", "value": 2},
                    {"id": 41, "text": "Очень редко", "value": 1},
                    {"id": 42, "text": "Никогда", "value": 0}
                ]
            },
            {
                "id": 8,
                "question_number": 8,
                "text": "Я чувствую себя 'выгоревшим' из-за своей работы",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 43, "text": "Никогда", "value": 0},
                    {"id": 44, "text": "Очень редко", "value": 1},
                    {"id": 45, "text": "Иногда", "value": 2},
                    {"id": 46, "text": "Часто", "value": 3},
                    {"id": 47, "text": "Очень часто", "value": 4},
                    {"id": 48, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 9,
                "question_number": 9,
                "text": "Я чувствую, что моя работа положительно влияет на других людей",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 49, "text": "Всегда", "value": 5},
                    {"id": 50, "text": "Очень часто", "value": 4},
                    {"id": 51, "text": "Часто", "value": 3},
                    {"id": 52, "text": "Иногда", "value": 2},
                    {"id": 53, "text": "Очень редко", "value": 1},
                    {"id": 54, "text": "Никогда", "value": 0}
                ]
            },
            {
                "id": 10,
                "question_number": 10,
                "text": "С некоторых пор я стал более черствым по отношению к людям, с которыми работаю",
                "subscale": "Деперсонализация",
                "options": [
                    {"id": 55, "text": "Никогда", "value": 0},
                    {"id": 56, "text": "Очень редко", "value": 1},
                    {"id": 57, "text": "Иногда", "value": 2},
                    {"id": 58, "text": "Часто", "value": 3},
                    {"id": 59, "text": "Очень часто", "value": 4},
                    {"id": 60, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 11,
                "question_number": 11,
                "text": "Я беспокоюсь, что эта работа ожесточает меня эмоционально",
                "subscale": "Деперсонализация",
                "options": [
                    {"id": 61, "text": "Никогда", "value": 0},
                    {"id": 62, "text": "Очень редко", "value": 1},
                    {"id": 63, "text": "Иногда", "value": 2},
                    {"id": 64, "text": "Часто", "value": 3},
                    {"id": 65, "text": "Очень часто", "value": 4},
                    {"id": 66, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 12,
                "question_number": 12,
                "text": "У меня много планов и идей относительно своей работы",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 67, "text": "Всегда", "value": 5},
                    {"id": 68, "text": "Очень часто", "value": 4},
                    {"id": 69, "text": "Часто", "value": 3},
                    {"id": 70, "text": "Иногда", "value": 2},
                    {"id": 71, "text": "Очень редко", "value": 1},
                    {"id": 72, "text": "Никогда", "value": 0}
                ]
            },
            {
                "id": 13,
                "question_number": 13,
                "text": "Я чувствую себя на пределе своих возможностей",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 73, "text": "Никогда", "value": 0},
                    {"id": 74, "text": "Очень редко", "value": 1},
                    {"id": 75, "text": "Иногда", "value": 2},
                    {"id": 76, "text": "Часто", "value": 3},
                    {"id": 77, "text": "Очень часто", "value": 4},
                    {"id": 78, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 14,
                "question_number": 14,
                "text": "Моя работа все больше и больше меня разочаровывает",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 79, "text": "Никогда", "value": 0},
                    {"id": 80, "text": "Очень редко", "value": 1},
                    {"id": 81, "text": "Иногда", "value": 2},
                    {"id": 82, "text": "Часто", "value": 3},
                    {"id": 83, "text": "Очень часто", "value": 4},
                    {"id": 84, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 15,
                "question_number": 15,
                "text": "Мне кажется, что я слишком много работаю",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 85, "text": "Никогда", "value": 0},
                    {"id": 86, "text": "Очень редко", "value": 1},
                    {"id": 87, "text": "Иногда", "value": 2},
                    {"id": 88, "text": "Часто", "value": 3},
                    {"id": 89, "text": "Очень часто", "value": 4},
                    {"id": 90, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 16,
                "question_number": 16,
                "text": "Мне неинтересно то, что происходит с моими подопечными (клиентами, пациентами, учениками)",
                "subscale": "Деперсонализация",
                "options": [
                    {"id": 91, "text": "Никогда", "value": 0},
                    {"id": 92, "text": "Очень редко", "value": 1},
                    {"id": 93, "text": "Иногда", "value": 2},
                    {"id": 94, "text": "Часто", "value": 3},
                    {"id": 95, "text": "Очень часто", "value": 4},
                    {"id": 96, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 17,
                "question_number": 17,
                "text": "Работать непосредственно с людьми для меня слишком тяжело",
                "subscale": "Эмоциональное истощение",
                "options": [
                    {"id": 97, "text": "Никогда", "value": 0},
                    {"id": 98, "text": "Очень редко", "value": 1},
                    {"id": 99, "text": "Иногда", "value": 2},
                    {"id": 100, "text": "Часто", "value": 3},
                    {"id": 101, "text": "Очень часто", "value": 4},
                    {"id": 102, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 18,
                "question_number": 18,
                "text": "Я легко создаю на работе расслабленную атмосферу",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 103, "text": "Всегда", "value": 5},
                    {"id": 104, "text": "Очень часто", "value": 4},
                    {"id": 105, "text": "Часто", "value": 3},
                    {"id": 106, "text": "Иногда", "value": 2},
                    {"id": 107, "text": "Очень редко", "value": 1},
                    {"id": 108, "text": "Никогда", "value": 0}
                ]
            },
            {
                "id": 19,
                "question_number": 19,
                "text": "Я чувствую себя бодрым после общения со своими подопечными (клиентами, пациентами, учениками)",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 109, "text": "Всегда", "value": 5},
                    {"id": 110, "text": "Очень часто", "value": 4},
                    {"id": 111, "text": "Часто", "value": 3},
                    {"id": 112, "text": "Иногда", "value": 2},
                    {"id": 113, "text": "Очень редко", "value": 1},
                    {"id": 114, "text": "Никогда", "value": 0}
                ]
            },
            {
                "id": 20,
                "question_number": 20,
                "text": "Я сделал много стоящего в этой профессии",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 115, "text": "Всегда", "value": 5},
                    {"id": 116, "text": "Очень часто", "value": 4},
                    {"id": 117, "text": "Часто", "value": 3},
                    {"id": 118, "text": "Иногда", "value": 2},
                    {"id": 119, "text": "Очень редко", "value": 1},
                    {"id": 120, "text": "Никогда", "value": 0}
                ]
            },
            {
                "id": 21,
                "question_number": 21,
                "text": "Я чувствую, что мои подопечные (клиенты, пациенты, ученики) винят меня в своих проблемах",
                "subscale": "Деперсонализация",
                "options": [
                    {"id": 121, "text": "Никогда", "value": 0},
                    {"id": 122, "text": "Очень редко", "value": 1},
                    {"id": 123, "text": "Иногда", "value": 2},
                    {"id": 124, "text": "Часто", "value": 3},
                    {"id": 125, "text": "Очень часто", "value": 4},
                    {"id": 126, "text": "Всегда", "value": 5}
                ]
            },
            {
                "id": 22,
                "question_number": 22,
                "text": "В последнее время я стал хуже работать",
                "subscale": "Редукция достижений",
                "options": [
                    {"id": 127, "text": "Никогда", "value": 0},
                    {"id": 128, "text": "Очень редко", "value": 1},
                    {"id": 129, "text": "Иногда", "value": 2},
                    {"id": 130, "text": "Часто", "value": 3},
                    {"id": 131, "text": "Очень часто", "value": 4},
                    {"id": 132, "text": "Всегда", "value": 5}
                ]
            }
        ]

    def calculate(self, answers: list) -> dict:
        """Рассчитать результаты теста"""
        # Разделяем ответы по субшкалам
        emotional_exhaustion = 0
        depersonalization = 0
        personal_accomplishment = 0

        # Вопросы эмоционального истощения: 1, 2, 3, 6, 8, 13, 14, 16, 20
        ee_questions = [1, 2, 3, 6, 8, 13, 14, 16, 20]
        # Вопросы деперсонализации: 5, 10, 11, 15, 22
        dp_questions = [5, 10, 11, 15, 22]
        # Вопросы редукции достижений: 4, 7, 9, 12, 17, 18, 19, 21
        pa_questions = [4, 7, 9, 12, 17, 18, 19, 21]

        for answer in answers:
            question_id = answer.get("question_id")
            value = answer.get("value", 0)

            if question_id in ee_questions:
                emotional_exhaustion += value
            elif question_id in dp_questions:
                depersonalization += value
            elif question_id in pa_questions:
                personal_accomplishment += value

        total_score = emotional_exhaustion + depersonalization + personal_accomplishment

        # Определение уровня выгорания
        ee_level = self._get_ee_level(emotional_exhaustion)
        dp_level = self._get_dp_level(depersonalization)
        pa_level = self._get_pa_level(personal_accomplishment)

        overall_level = self._get_overall_level(ee_level, dp_level, pa_level)

        interpretation = f"Эмоциональное истощение: {ee_level} ({emotional_exhaustion} баллов), Деперсонализация: {dp_level} ({depersonalization} баллов), Редукция достижений: {pa_level} ({personal_accomplishment} баллов)"

        return {
            "total_score": total_score,
            "burnout_level": overall_level,
            "subscale_scores": {
                "Эмоциональное истощение": emotional_exhaustion,
                "Деперсонализация": depersonalization,
                "Редукция достижений": personal_accomplishment
            },
            "subscale_levels": {
                "Эмоциональное истощение": ee_level,
                "Деперсонализация": dp_level,
                "Редукция достижений": pa_level
            },
            "interpretation": interpretation,
            "recommendations": self._get_recommendations(ee_level, dp_level, pa_level)
        }

    def _get_ee_level(self, score: int) -> str:
        if score <= 16:
            return "Низкий"
        elif score <= 24:
            return "Средний"
        else:
            return "Высокий"

    def _get_dp_level(self, score: int) -> str:
        if score <= 6:
            return "Низкий"
        elif score <= 11:
            return "Средний"
        else:
            return "Высокий"

    def _get_pa_level(self, score: int) -> str:
        if score >= 30:
            return "Высокий"
        elif score >= 18:
            return "Средний"
        else:
            return "Низкий"

    def _get_overall_level(self, ee_level: str, dp_level: str, pa_level: str) -> str:
        if ee_level == "Высокий" and dp_level == "Высокий" and pa_level == "Низкий":
            return "Высокий уровень выгорания"
        elif (ee_level == "Высокий" and dp_level == "Высокий") or (ee_level == "Высокий" and pa_level == "Низкий") or (
                dp_level == "Высокий" and pa_level == "Низкий"):
            return "Умеренный уровень выгорания"
        elif ee_level == "Высокий" or dp_level == "Высокий" or pa_level == "Низкий":
            return "Низкий уровень выгорания"
        else:
            return "Отсутствие выгорания"

    def _get_recommendations(self, ee_level: str, dp_level: str, pa_level: str) -> list:
        recommendations = []

        if ee_level == "Высокий":
            recommendations.extend([
                "Снижение рабочей нагрузки и пересмотр приоритетов",
                "Регулярные перерывы в работе каждые 1.5-2 часа",
                "Техники релаксации и медитации (10-15 минут в день)",
                "Достаточный сон (7-8 часов) и полноценный отдых",
                "Физическая активность (минимум 30 минут в день)"
            ])

        if dp_level == "Высокий":
            recommendations.extend([
                "Тренинги по эмпатии и коммуникации",
                "Супервизия или консультации с коллегами",
                "Работа над установлением профессиональных границ",
                "Поиск смысла в работе и профессиональных ценностей",
                "Развитие эмоционального интеллекта"
            ])

        if pa_level == "Низкий":
            recommendations.extend([
                "Постановка достижимых краткосрочных целей",
                "Ведение дневника профессиональных успехов",
                "Повышение квалификации и профессиональное развитие",
                "Поиск новых вызовов и задач в работе",
                "Получение обратной связи от коллег и руководства"
            ])

        if not recommendations:
            recommendations = [
                "Продолжайте поддерживать баланс между работой и отдыхом",
                "Регулярно оценивайте свое эмоциональное состояние",
                "Обращайтесь за помощью к коллегам или специалистам при необходимости",
                "Практикуйте техники саморегуляции и стресс-менеджмента"
            ]

        return recommendations