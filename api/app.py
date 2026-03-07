from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
import os

app = FastAPI()

# Get the path to the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def homepage():
    return FileResponse(os.path.join(BASE__DIR, "index.html"))

@app.get("/api/band")
def generate_band(city: str, pet: str):
    script_path = os.path.join(BASE_DIR, "day1.py")
    process = subprocess.Popen(
        ["python3", script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    # feed inputs to the script
    output, error = process.communicate(f"{city}\n{pet}\n")
    return {"result": output}
