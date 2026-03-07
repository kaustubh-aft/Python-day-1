from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.get("/")
def homepage():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

@app.get("/api/band")
def generate_band(city: str, pet: str):
    band_name = f"{city.strip()} {pet.strip()}"
    return {"result": band_name}
