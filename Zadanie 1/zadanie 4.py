#zadanie 1.4
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

class Numbers(BaseModel):
    num1: float
    num2: float

app = FastAPI()
user = User(name="Иван Петров", id=1)

@app.get("/users")
async def get_user():
    return user

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}