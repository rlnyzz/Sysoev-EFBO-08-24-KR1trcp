#zadanie 1.2
from fastapi import FastAPI
from fastapi.responses import FileResponse

@app = FastAPI()
app.get("/")
async def root():
    return FileResponse("zadanie2.html")