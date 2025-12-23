# app/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, JSON
from sqlalchemy.sql import func
from app.database import Base


class TestResult(Base):
    """Модель для сохранения результатов тестов"""
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    test_code = Column(String, nullable=False)
    test_name = Column(String, nullable=False)
    total_score = Column(Float, nullable=False)
    answers = Column(JSON)  # Сохраняем ответы в формате JSON
    interpretation = Column(Text)
    recommendations = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    session_id = Column(String, index=True)

    # Связь с пользователем (просто внешний ключ, без relationship)
    user_id = Column(Integer, nullable=True)  # nullable для анонимных пользователей