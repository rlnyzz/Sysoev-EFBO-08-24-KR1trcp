from fastapi import FastAPI, FileResponse
from pydantic import BaseModel, Field, field_validator
from typing import List
import re


class User(BaseModel):
    name: str
    id: int

class Numbers(BaseModel):
    num1: float
    num2: float

class AgeUser(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    
    @field_validator('message')
    @classmethod
    def validate_message(cls, v: str) -> str:
        forbidden_words = ['бляха-муха', 'кринге', 'СУмочКА']
        message_lower = v.lower()
        
        for word in forbidden_words:
            if re.search(r'\b' + re.escape(word) + r'\b', message_lower):
                raise ValueError('Использование недопустимых слов')
        
        return v

app = FastAPI()
feedback_storage: List[Feedback] = []
user = User(name="Сысоев Виталий", id=1)

@app.get("/")
async def root():
    return FileResponse("zadanie2.html")

@app.get("/users")
async def get_user():
    return user

@app.post("/calculate")
async def calculate(numbers: Numbers):
    return {"result": numbers.num1 + numbers.num2}

@app.post("/user")
async def check_user(user_data: AgeUser):
    return {
        "name": user_data.name,
        "age": user_data.age,
        "is_adult": user_data.age >= 18
    }

@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }

@app.get("/feedback/all", response_model=List[Feedback])
async def get_all_feedback():
    """просмотр всех отзывов"""
    return feedback_storage

@app.get("/feedback/stats")
async def get_feedback_stats():
    """статистика по отзывам"""
    if not feedback_storage:
        return {"total_feedbacks": 0}
    return {
        "total_feedbacks": len(feedback_storage),
        "average_message_length": sum(len(f.message) for f in feedback_storage) / len(feedback_storage)
    }