"""
Шкала тревоги Спилбергера-Ханина
40 вопросов (20 на реактивную тревожность + 20 на личностную тревожность)
Диапазон баллов: 20-80
"""


class SpielbergerTest:
    """Класс для работы с тестом Спилбергера-Ханина"""

    def __init__(self):
        self.code = "spielberger"
        self.name = "Шкала тревоги Спилбергера-Ханина"
        self.description = "Измерение тревожности как состояния (реактивная тревожность) и как свойства (личностная тревожность)"
        self.instructions = "Прочитайте каждое утверждение и выберите ответ, который наилучшим образом описывает ваше обычное состояние."
        self.questions_count = 40
        self.min_score = 20
        self.max_score = 80
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
                "text": "Я спокоен",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 1, "text": "Почти никогда", "value": 1},
                    {"id": 2, "text": "Иногда", "value": 2},
                    {"id": 3, "text": "Часто", "value": 3},
                    {"id": 4, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 2,
                "question_number": 2,
                "text": "Мне ничто не угрожает",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 5, "text": "Почти никогда", "value": 1},
                    {"id": 6, "text": "Иногда", "value": 2},
                    {"id": 7, "text": "Часто", "value": 3},
                    {"id": 8, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 3,
                "question_number": 3,
                "text": "Я нахожусь в напряжении",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 9, "text": "Почти никогда", "value": 1},
                    {"id": 10, "text": "Иногда", "value": 2},
                    {"id": 11, "text": "Часто", "value": 3},
                    {"id": 12, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 4,
                "question_number": 4,
                "text": "Я внутренне скован",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 13, "text": "Почти никогда", "value": 1},
                    {"id": 14, "text": "Иногда", "value": 2},
                    {"id": 15, "text": "Часто", "value": 3},
                    {"id": 16, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 5,
                "question_number": 5,
                "text": "Я чувствую себя свободно",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 17, "text": "Почти никогда", "value": 1},
                    {"id": 18, "text": "Иногда", "value": 2},
                    {"id": 19, "text": "Часто", "value": 3},
                    {"id": 20, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 6,
                "question_number": 6,
                "text": "Я расстроен",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 21, "text": "Почти никогда", "value": 1},
                    {"id": 22, "text": "Иногда", "value": 2},
                    {"id": 23, "text": "Часто", "value": 3},
                    {"id": 24, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 7,
                "question_number": 7,
                "text": "Меня волнуют возможные неудачи",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 25, "text": "Почти никогда", "value": 1},
                    {"id": 26, "text": "Иногда", "value": 2},
                    {"id": 27, "text": "Часто", "value": 3},
                    {"id": 28, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 8,
                "question_number": 8,
                "text": "Я чувствую себя отдохнувшим",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 29, "text": "Почти никогда", "value": 1},
                    {"id": 30, "text": "Иногда", "value": 2},
                    {"id": 31, "text": "Часто", "value": 3},
                    {"id": 32, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 9,
                "question_number": 9,
                "text": "Я встревожен",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 33, "text": "Почти никогда", "value": 1},
                    {"id": 34, "text": "Иногда", "value": 2},
                    {"id": 35, "text": "Часто", "value": 3},
                    {"id": 36, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 10,
                "question_number": 10,
                "text": "Я испытываю чувство внутреннего удовлетворения",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 37, "text": "Почти никогда", "value": 1},
                    {"id": 38, "text": "Иногда", "value": 2},
                    {"id": 39, "text": "Часто", "value": 3},
                    {"id": 40, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 11,
                "question_number": 11,
                "text": "Я уверен в себе",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 41, "text": "Почти никогда", "value": 1},
                    {"id": 42, "text": "Иногда", "value": 2},
                    {"id": 43, "text": "Часто", "value": 3},
                    {"id": 44, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 12,
                "question_number": 12,
                "text": "Я нервничаю",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 45, "text": "Почти никогда", "value": 1},
                    {"id": 46, "text": "Иногда", "value": 2},
                    {"id": 47, "text": "Часто", "value": 3},
                    {"id": 48, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 13,
                "question_number": 13,
                "text": "Я не нахожу себе места",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 49, "text": "Почти никогда", "value": 1},
                    {"id": 50, "text": "Иногда", "value": 2},
                    {"id": 51, "text": "Часто", "value": 3},
                    {"id": 52, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 14,
                "question_number": 14,
                "text": "Я взвинчен",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 53, "text": "Почти никогда", "value": 1},
                    {"id": 54, "text": "Иногда", "value": 2},
                    {"id": 55, "text": "Часто", "value": 3},
                    {"id": 56, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 15,
                "question_number": 15,
                "text": "Я не чувствую скованности, напряжения",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 57, "text": "Почти никогда", "value": 1},
                    {"id": 58, "text": "Иногда", "value": 2},
                    {"id": 59, "text": "Часто", "value": 3},
                    {"id": 60, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 16,
                "question_number": 16,
                "text": "Я доволен",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 61, "text": "Почти никогда", "value": 1},
                    {"id": 62, "text": "Иногда", "value": 2},
                    {"id": 63, "text": "Часто", "value": 3},
                    {"id": 64, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 17,
                "question_number": 17,
                "text": "Я озабочен",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 65, "text": "Почти никогда", "value": 1},
                    {"id": 66, "text": "Иногда", "value": 2},
                    {"id": 67, "text": "Часто", "value": 3},
                    {"id": 68, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 18,
                "question_number": 18,
                "text": "Я слишком возбужден и мне не по себе",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 69, "text": "Почти никогда", "value": 1},
                    {"id": 70, "text": "Иногда", "value": 2},
                    {"id": 71, "text": "Часто", "value": 3},
                    {"id": 72, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 19,
                "question_number": 19,
                "text": "Мне радостно",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 73, "text": "Почти никогда", "value": 1},
                    {"id": 74, "text": "Иногда", "value": 2},
                    {"id": 75, "text": "Часто", "value": 3},
                    {"id": 76, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 20,
                "question_number": 20,
                "text": "Мне приятно",
                "subscale": "Реактивная тревожность",
                "options": [
                    {"id": 77, "text": "Почти никогда", "value": 1},
                    {"id": 78, "text": "Иногда", "value": 2},
                    {"id": 79, "text": "Часто", "value": 3},
                    {"id": 80, "text": "Почти всегда", "value": 4}
                ]
            },
            # Личностная тревожность (вопросы 21-40)
            {
                "id": 21,
                "question_number": 21,
                "text": "Я часто испытываю удовольствие",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 81, "text": "Почти никогда", "value": 1},
                    {"id": 82, "text": "Иногда", "value": 2},
                    {"id": 83, "text": "Часто", "value": 3},
                    {"id": 84, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 22,
                "question_number": 22,
                "text": "Я бываю раздражительным",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 85, "text": "Почти никогда", "value": 1},
                    {"id": 86, "text": "Иногда", "value": 2},
                    {"id": 87, "text": "Часто", "value": 3},
                    {"id": 88, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 23,
                "question_number": 23,
                "text": "Я легко могу расстроиться",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 89, "text": "Почти никогда", "value": 1},
                    {"id": 90, "text": "Иногда", "value": 2},
                    {"id": 91, "text": "Часто", "value": 3},
                    {"id": 92, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 24,
                "question_number": 24,
                "text": "Я хотел бы быть таким же удачливым, как и другие",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 93, "text": "Почти никогда", "value": 1},
                    {"id": 94, "text": "Иногда", "value": 2},
                    {"id": 95, "text": "Часто", "value": 3},
                    {"id": 96, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 25,
                "question_number": 25,
                "text": "Я сильно переживаю неприятности и долго не могу о них забыть",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 97, "text": "Почти никогда", "value": 1},
                    {"id": 98, "text": "Иногда", "value": 2},
                    {"id": 99, "text": "Часто", "value": 3},
                    {"id": 100, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 26,
                "question_number": 26,
                "text": "Я чувствую прилив сил, желание работать",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 101, "text": "Почти никогда", "value": 1},
                    {"id": 102, "text": "Иногда", "value": 2},
                    {"id": 103, "text": "Часто", "value": 3},
                    {"id": 104, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 27,
                "question_number": 27,
                "text": "Я обычно спокоен и меня нелегко расстроить",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 105, "text": "Почти никогда", "value": 1},
                    {"id": 106, "text": "Иногда", "value": 2},
                    {"id": 107, "text": "Часто", "value": 3},
                    {"id": 108, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 28,
                "question_number": 28,
                "text": "Меня часто мучают страхи и дурные предчувствия",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 109, "text": "Почти никогда", "value": 1},
                    {"id": 110, "text": "Иногда", "value": 2},
                    {"id": 111, "text": "Часто", "value": 3},
                    {"id": 112, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 29,
                "question_number": 29,
                "text": "Я часто бываю недоволен",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 113, "text": "Почти никогда", "value": 1},
                    {"id": 114, "text": "Иногда", "value": 2},
                    {"id": 115, "text": "Часто", "value": 3},
                    {"id": 116, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 30,
                "question_number": 30,
                "text": "У меня бывают приступы паники",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 117, "text": "Почти никогда", "value": 1},
                    {"id": 118, "text": "Иногда", "value": 2},
                    {"id": 119, "text": "Часто", "value": 3},
                    {"id": 120, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 31,
                "question_number": 31,
                "text": "Я обычно устаю",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 121, "text": "Почти никогда", "value": 1},
                    {"id": 122, "text": "Иногда", "value": 2},
                    {"id": 123, "text": "Часто", "value": 3},
                    {"id": 124, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 32,
                "question_number": 32,
                "text": "Я обычно чувствую себя вполне счастливым",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 125, "text": "Почти никогда", "value": 1},
                    {"id": 126, "text": "Иногда", "value": 2},
                    {"id": 127, "text": "Часто", "value": 3},
                    {"id": 128, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 33,
                "question_number": 33,
                "text": "В незнакомой обстановке я чувствую себя скованно",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 129, "text": "Почти никогда", "value": 1},
                    {"id": 130, "text": "Иногда", "value": 2},
                    {"id": 131, "text": "Часто", "value": 3},
                    {"id": 132, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 34,
                "question_number": 34,
                "text": "Мне не хватает уверенности в себе",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 133, "text": "Почти никогда", "value": 1},
                    {"id": 134, "text": "Иногда", "value": 2},
                    {"id": 135, "text": "Часто", "value": 3},
                    {"id": 136, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 35,
                "question_number": 35,
                "text": "Обычно я чувствую себя в безопасности",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 137, "text": "Почти никогда", "value": 1},
                    {"id": 138, "text": "Иногда", "value": 2},
                    {"id": 139, "text": "Часто", "value": 3},
                    {"id": 140, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 36,
                "question_number": 36,
                "text": "Я стараюсь избегать критических ситуаций и трудностей",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 141, "text": "Почти никогда", "value": 1},
                    {"id": 142, "text": "Иногда", "value": 2},
                    {"id": 143, "text": "Часто", "value": 3},
                    {"id": 144, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 37,
                "question_number": 37,
                "text": "У меня бывает меланхолия (тоска)",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 145, "text": "Почти никогда", "value": 1},
                    {"id": 146, "text": "Иногда", "value": 2},
                    {"id": 147, "text": "Часто", "value": 3},
                    {"id": 148, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 38,
                "question_number": 38,
                "text": "Я доволен",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 149, "text": "Почти никогда", "value": 1},
                    {"id": 150, "text": "Иногда", "value": 2},
                    {"id": 151, "text": "Часто", "value": 3},
                    {"id": 152, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 39,
                "question_number": 39,
                "text": "Любые неожиданности выводят меня из равновесия",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 153, "text": "Почти никогда", "value": 1},
                    {"id": 154, "text": "Иногда", "value": 2},
                    {"id": 155, "text": "Часто", "value": 3},
                    {"id": 156, "text": "Почти всегда", "value": 4}
                ]
            },
            {
                "id": 40,
                "question_number": 40,
                "text": "Я бываю вполне счастлив",
                "subscale": "Личностная тревожность",
                "options": [
                    {"id": 157, "text": "Почти никогда", "value": 1},
                    {"id": 158, "text": "Иногда", "value": 2},
                    {"id": 159, "text": "Часто", "value": 3},
                    {"id": 160, "text": "Почти всегда", "value": 4}
                ]
            }
        ]

    def calculate(self, answers: list) -> dict:
        """Рассчитать результаты теста"""
        # Разделение на реактивную (вопросы 1-20) и личностную (21-40) тревожность
        reactive_anxiety = 0
        personal_anxiety = 0

        for answer in answers:
            question_id = answer.get("question_id")
            value = answer.get("value", 0)

            if question_id <= 20:
                reactive_anxiety += value
            else:
                personal_anxiety += value

        total_score = reactive_anxiety + personal_anxiety

        # Определение уровней тревожности
        reactive_level = self._get_anxiety_level(reactive_anxiety, is_reactive=True)
        personal_level = self._get_anxiety_level(personal_anxiety, is_reactive=False)

        interpretation = self._get_interpretation(reactive_level, personal_level)

        return {
            "total_score": total_score,
            "reactive_anxiety": reactive_anxiety,
            "personal_anxiety": personal_anxiety,
            "reactive_level": reactive_level,
            "personal_level": personal_level,
            "interpretation": interpretation,
            "recommendations": self._get_recommendations(reactive_level, personal_level)
        }

    def _get_anxiety_level(self, score: int, is_reactive: bool = True) -> str:
        """Определить уровень тревожности"""
        if is_reactive:
            # Реактивная тревожность (максимум 80)
            if score <= 30:
                return "Низкая тревожность"
            elif score <= 45:
                return "Умеренная тревожность"
            elif score <= 60:
                return "Высокая тревожность"
            else:
                return "Очень высокая тревожность"
        else:
            # Личностная тревожность (максимум 80)
            if score <= 30:
                return "Низкая тревожность"
            elif score <= 45:
                return "Умеренная тревожность"
            elif score <= 60:
                return "Высокая тревожность"
            else:
                return "Очень высокая тревожность"

    def _get_interpretation(self, reactive_level: str, personal_level: str) -> str:
        """Получить интерпретацию результатов"""
        interpretations = {
            ("Низкая тревожность", "Низкая тревожность"):
                "У вас низкий уровень как ситуативной, так и личностной тревожности. Вы хорошо справляетесь со стрессовыми ситуациями и в целом чувствуете себя спокойно.",

            ("Низкая тревожность", "Умеренная тревожность"):
                "У вас низкий уровень ситуативной тревожности, но умеренный уровень личностной тревожности. Вы хорошо справляетесь с конкретными стрессовыми ситуациями, но в целом склонны к тревоге.",

            ("Умеренная тревожность", "Низкая тревожность"):
                "У вас умеренный уровень ситуативной тревожности при низком уровне личностной тревожности. Вы испытываете тревогу в конкретных стрессовых ситуациях, но в целом чувствуете себя спокойно.",

            ("Умеренная тревожность", "Умеренная тревожность"):
                "У вас умеренный уровень как ситуативной, так и личностной тревожности. Вы испытываете умеренную тревогу в стрессовых ситуациях и в целом склонны к тревожным реакциям.",

            ("Высокая тревожность", "Высокая тревожность"):
                "У вас высокий уровень как ситуативной, так и личностной тревожности. Рекомендуется обратить внимание на методы управления тревогой и рассмотреть возможность консультации специалиста.",

            ("Очень высокая тревожность", "Очень высокая тревожность"):
                "У вас очень высокий уровень тревожности. Это может значительно влиять на качество жизни. Рекомендуется обратиться за профессиональной помощью."
        }

        return interpretations.get(
            (reactive_level, personal_level),
            f"Реактивная тревожность: {reactive_level}, Личностная тревожность: {personal_level}"
        )

    def _get_recommendations(self, reactive_level: str, personal_level: str) -> list:
        """Получить рекомендации на основе результатов"""
        recommendations = []

        # Рекомендации для реактивной тревожности
        if reactive_level in ["Высокая тревожность", "Очень высокая тревожность"]:
            recommendations.extend([
                "Техники релаксации и дыхательные упражнения в стрессовых ситуациях",
                "Практика mindfulness и медитации",
                "Регулярная физическая активность для снижения стресса",
                "Обучение техникам когнитивной переоценки стрессовых ситуаций"
            ])

        # Рекомендации для личностной тревожности
        if personal_level in ["Высокая тревожность", "Очень высокая тревожность"]:
            recommendations.extend([
                "Когнитивно-поведенческая терапия для работы с тревожными паттернами",
                "Регулярная практика техник саморегуляции",
                "Развитие навыков совладания со стрессом",
                "Консультация психолога или психотерапевта"
            ])

        # Общие рекомендации
        if not recommendations:
            recommendations = [
                "Продолжайте практиковать здоровые способы совладания со стрессом",
                "Регулярно оценивайте свое эмоциональное состояние",
                "Поддерживайте баланс между работой и отдыхом",
                "Обращайтесь за помощью при необходимости"
            ]

        # Добавить общие рекомендации для всех уровней
        recommendations.extend([
            "Регулярный сон (7-8 часов в сутки)",
            "Сбалансированное питание",
            "Поддержание социальных связей",
            "Хобби и интересы вне работы"
        ])

        return recommendations