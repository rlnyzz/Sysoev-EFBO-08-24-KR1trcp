#zadanie 1.5
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/user")
async def check_user(user: User):
    is_adult = user.age >= 18
    
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }