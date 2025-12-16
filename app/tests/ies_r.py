"""
IES-R (Impact of Event Scale - Revised) - Опросник для диагностики ПТСР
22 вопроса, диапазон баллов: 0-88
"""


class IESRTest:
    """Класс для работы с тестом IES-R"""

    def __init__(self):
        self.code = "ies_r"
        self.name = "Опросник для диагностики ПТСР (IES-R)"
        self.description = "Оценка симптомов посттравматического стрессового расстройства: вторжение, избегание, гиперактивность"
        self.instructions = "Оцените, насколько вас беспокоили следующие переживания за последние 7 дней."
        self.questions_count = 22
        self.min_score = 0
        self.max_score = 88
        self.time_limit = 10  # минут

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
                "text": "Любые напоминания вызывали у меня чувства, связанные с тем событием",
                "subscale": "Вторжение",
                "options": [
                    {"id": 1, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 2, "text": "Слегка", "value": 1},
                    {"id": 3, "text": "Умеренно", "value": 2},
                    {"id": 4, "text": "Довольно сильно", "value": 3},
                    {"id": 5, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 2,
                "question_number": 2,
                "text": "У меня были трудности с засыпанием или сном",
                "subscale": "Гиперактивность",
                "options": [
                    {"id": 6, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 7, "text": "Слегка", "value": 1},
                    {"id": 8, "text": "Умеренно", "value": 2},
                    {"id": 9, "text": "Довольно сильно", "value": 3},
                    {"id": 10, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 3,
                "question_number": 3,
                "text": "Другие вещи постоянно заставляли меня думать об этом",
                "subscale": "Вторжение",
                "options": [
                    {"id": 11, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 12, "text": "Слегка", "value": 1},
                    {"id": 13, "text": "Умеренно", "value": 2},
                    {"id": 14, "text": "Доворя сильно", "value": 3},
                    {"id": 15, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 4,
                "question_number": 4,
                "text": "Я чувствовал(а) раздражение и злость",
                "subscale": "Гиперактивность",
                "options": [
                    {"id": 16, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 17, "text": "Слегка", "value": 1},
                    {"id": 18, "text": "Умеренно", "value": 2},
                    {"id": 19, "text": "Доворя сильно", "value": 3},
                    {"id": 20, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 5,
                "question_number": 5,
                "text": "Я избегал(а) позволять себе испытывать чувства по поводу этого",
                "subscale": "Избегание",
                "options": [
                    {"id": 21, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 22, "text": "Слегка", "value": 1},
                    {"id": 23, "text": "Умеренно", "value": 2},
                    {"id": 24, "text": "Доворя сильно", "value": 3},
                    {"id": 25, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 6,
                "question_number": 6,
                "text": "У меня были мысли об этом, даже когда я не хотел(а) думать об этом",
                "subscale": "Вторжение",
                "options": [
                    {"id": 26, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 27, "text": "Слегка", "value": 1},
                    {"id": 28, "text": "Умеренно", "value": 2},
                    {"id": 29, "text": "Доворя сильно", "value": 3},
                    {"id": 30, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 7,
                "question_number": 7,
                "text": "Я чувствовал(а), как будто этого не было или это нереально",
                "subscale": "Оцепенение",
                "options": [
                    {"id": 31, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 32, "text": "Слегка", "value": 1},
                    {"id": 33, "text": "Умеренно", "value": 2},
                    {"id": 34, "text": "Доворя сильно", "value": 3},
                    {"id": 35, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 8,
                "question_number": 8,
                "text": "Я держался(ась) подальше от напоминаний об этом",
                "subscale": "Избегание",
                "options": [
                    {"id": 36, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 37, "text": "Слегка", "value": 1},
                    {"id": 38, "text": "Умеренно", "value": 2},
                    {"id": 39, "text": "Доворя сильно", "value": 3},
                    {"id": 40, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 9,
                "question_number": 9,
                "text": "Картинки этого события всплывали у меня в голове",
                "subscale": "Вторжение",
                "options": [
                    {"id": 41, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 42, "text": "Слегка", "value": 1},
                    {"id": 43, "text": "Умеренно", "value": 2},
                    {"id": 44, "text": "Доворя сильно", "value": 3},
                    {"id": 45, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 10,
                "question_number": 10,
                "text": "Я был(а) нервным(ой) и легко вздрагивал(а)",
                "subscale": "Гиперактивность",
                "options": [
                    {"id": 46, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 47, "text": "Слегка", "value": 1},
                    {"id": 48, "text": "Умеренно", "value": 2},
                    {"id": 49, "text": "Доворя сильно", "value": 3},
                    {"id": 50, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 11,
                "question_number": 11,
                "text": "Я старался(ась) не думать об этом",
                "subscale": "Избегание",
                "options": [
                    {"id": 51, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 52, "text": "Слегка", "value": 1},
                    {"id": 53, "text": "Умеренно", "value": 2},
                    {"id": 54, "text": "Доворя сильно", "value": 3},
                    {"id": 55, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 12,
                "question_number": 12,
                "text": "Я был(а) осведомлен(а) о том, что у меня все еще есть чувства по поводу этого, но я не разбирался(ась) с ними",
                "subscale": "Избегание",
                "options": [
                    {"id": 56, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 57, "text": "Слегка", "value": 1},
                    {"id": 58, "text": "Умеренно", "value": 2},
                    {"id": 59, "text": "Доворя сильно", "value": 3},
                    {"id": 60, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 13,
                "question_number": 13,
                "text": "Мои чувства по поводу этого были somewhat numb",
                "subscale": "Оцепенение",
                "options": [
                    {"id": 61, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 62, "text": "Слегка", "value": 1},
                    {"id": 63, "text": "Умеренно", "value": 2},
                    {"id": 64, "text": "Доворя сильно", "value": 3},
                    {"id": 65, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 14,
                "question_number": 14,
                "text": "Я обнаруживал(а), что веду себя или чувствую себя так, как будто я снова переживаю то событие",
                "subscale": "Вторжение",
                "options": [
                    {"id": 66, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 67, "text": "Слегка", "value": 1},
                    {"id": 68, "text": "Умеренно", "value": 2},
                    {"id": 69, "text": "Доворя сильно", "value": 3},
                    {"id": 70, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 15,
                "question_number": 15,
                "text": "У меня были трудности с засыпанием",
                "subscale": "Гиперактивность",
                "options": [
                    {"id": 71, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 72, "text": "Слегка", "value": 1},
                    {"id": 73, "text": "Умеренно", "value": 2},
                    {"id": 74, "text": "Доворя сильно", "value": 3},
                    {"id": 75, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 16,
                "question_number": 16,
                "text": "У меня были сильные волны чувств по поводу этого",
                "subscale": "Вторжение",
                "options": [
                    {"id": 76, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 77, "text": "Слегка", "value": 1},
                    {"id": 78, "text": "Умеренно", "value": 2},
                    {"id": 79, "text": "Доворя сильно", "value": 3},
                    {"id": 80, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 17,
                "question_number": 17,
                "text": "Я старался(ась) избавиться от этого из памяти",
                "subscale": "Избегание",
                "options": [
                    {"id": 81, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 82, "text": "Слегка", "value": 1},
                    {"id": 83, "text": "Умеренно", "value": 2},
                    {"id": 84, "text": "Доворя сильно", "value": 3},
                    {"id": 85, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 18,
                "question_number": 18,
                "text": "У меня были трудности с концентрацией внимания",
                "subscale": "Гиперактивность",
                "options": [
                    {"id": 86, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 87, "text": "Слегка", "value": 1},
                    {"id": 88, "text": "Умеренно", "value": 2},
                    {"id": 89, "text": "Доворя сильно", "value": 3},
                    {"id": 90, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 19,
                "question_number": 19,
                "text": "Напоминания об этом вызывали у меня физические реакции, такие как потливость, трудности с дыханием, тошнота или сильное сердцебиение",
                "subscale": "Гиперактивность",
                "options": [
                    {"id": 91, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 92, "text": "Слегка", "value": 1},
                    {"id": 93, "text": "Умеренно", "value": 2},
                    {"id": 94, "text": "Доворя сильно", "value": 3},
                    {"id": 95, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 20,
                "question_number": 20,
                "text": "Мне снились кошмары об этом",
                "subscale": "Вторжение",
                "options": [
                    {"id": 96, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 97, "text": "Слегка", "value": 1},
                    {"id": 98, "text": "Умеренно", "value": 2},
                    {"id": 99, "text": "Доворя сильно", "value": 3},
                    {"id": 100, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 21,
                "question_number": 21,
                "text": "Я был(а) особенно бдителен(а) и насторожен(а)",
                "subscale": "Гиперактивность",
                "options": [
                    {"id": 101, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 102, "text": "Слегка", "value": 1},
                    {"id": 103, "text": "Умеренно", "value": 2},
                    {"id": 104, "text": "Доворя сильно", "value": 3},
                    {"id": 105, "text": "Очень сильно", "value": 4}
                ]
            },
            {
                "id": 22,
                "question_number": 22,
                "text": "Я старался(ась) не говорить об этом",
                "subscale": "Избегание",
                "options": [
                    {"id": 106, "text": "Совсем не беспокоило", "value": 0},
                    {"id": 107, "text": "Слегка", "value": 1},
                    {"id": 108, "text": "Умеренно", "value": 2},
                    {"id": 109, "text": "Доворя сильно", "value": 3},
                    {"id": 110, "text": "Очень сильно", "value": 4}
                ]
            }
        ]

    def calculate(self, answers: list) -> dict:
        """Рассчитать результаты теста"""
        total_score = sum(answer.get("value", 0) for answer in answers)

        # Расчет по субшкалам
        intrusion = 0
        avoidance = 0
        hyperarousal = 0

        # Вопросы вторжения: 1, 2, 3, 6, 9, 14, 16, 20
        intrusion_questions = [1, 2, 3, 6, 9, 14, 16, 20]
        # Вопросы избегания: 5, 7, 8, 11, 12, 13, 17, 22
        avoidance_questions = [5, 7, 8, 11, 12, 13, 17, 22]
        # Вопросы гиперактивности: 4, 10, 15, 18, 19, 21
        hyperarousal_questions = [4, 10, 15, 18, 19, 21]

        for answer in answers:
            question_id = answer.get("question_id")
            value = answer.get("value", 0)

            if question_id in intrusion_questions:
                intrusion += value
            elif question_id in avoidance_questions:
                avoidance += value
            elif question_id in hyperarousal_questions:
                hyperarousal += value

        # Определение уровня ПТСР
        if total_score <= 23:
            ptsd_level = "Минимальные симптомы ПТСР"
            interpretation = "Симптомы посттравматического стрессового расстройства минимальны или отсутствуют."
        elif total_score <= 32:
            ptsd_level = "Умеренные симптомы ПТСР"
            interpretation = "Наблюдаются умеренные симптомы ПТСР. Рекомендуется консультация специалиста."
        elif total_score <= 37:
            ptsd_level = "Выраженные симптомы ПТСР"
            interpretation = "Выраженные симптомы ПТСР. Необходима профессиональная помощь."
        else:
            ptsd_level = "Тяжелые симптомы ПТСР"
            interpretation = "Тяжелые симптомы ПТСР. Требуется срочная помощь специалиста."

        recommendations = self._get_recommendations(total_score)

        return {
            "total_score": total_score,
            "ptsd_level": ptsd_level,
            "interpretation": interpretation,
            "subscale_scores": {
                "Вторжение": intrusion,
                "Избегание": avoidance,
                "Гиперактивность": hyperarousal
            },
            "recommendations": recommendations
        }

    def _get_recommendations(self, score: int) -> list:
        if score <= 23:
            return [
                "Продолжайте практиковать здоровые способы совладания со стрессом",
                "Регулярная физическая активность",
                "Техники релаксации и медитации",
                "Поддержание социальных связей"
            ]
        elif score <= 32:
            return [
                "Консультация психолога или психотерапевта",
                "Терапия, ориентированная на травму",
                "Техники заземления и саморегуляции",
                "Избегание триггерных ситуаций",
                "Поддержка близких людей"
            ]
        elif score <= 37:
            return [
                "Консультация врача-психиатра",
                "Специализированная психотерапия ПТСР",
                "Техники управления тревогой",
                "Регулярная практика техник релаксации",
                "Создание безопасной поддерживающей среды"
            ]
        else:
            return [
                "СРОЧНАЯ КОНСУЛЬТАЦИЯ ВРАЧА-ПСИХИАТРА",
                "Специализированное лечение ПТСР",
                "Кризисная поддержка",
                "Не оставайтесь в одиночестве",
                "Телефон доверия: 8-800-2000-122",
                "Обратитесь в специализированный центр помощи"
            ]