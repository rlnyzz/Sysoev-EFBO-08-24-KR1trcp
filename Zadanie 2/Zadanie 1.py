#zadanie 2.1
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

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
    name: str
    message: str

app = FastAPI()

#Хранилище
feedback_storage = []
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
async def check_user(user: AgeUser):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }

@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

@app.get("/feedback/all")
async def get_all_feedback():
    return feedback_storage