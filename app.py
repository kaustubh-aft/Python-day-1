<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess

app = FastAPI()


# Serve the interactive webpage
@app.get("/")
def homepage():
    return FileResponse("index.html")


# API endpoint that runs your python script
@app.get("/band")
def generate_band(city: str, pet: str):

    process = subprocess.Popen(
        ["python", "day1.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # feed inputs to the script
    output, error = process.communicate(f"{city}\n{pet}\n")

    return {"result": output}
=======
from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/band")
def generate_band(city: str, pet: str):

    process = subprocess.Popen(
        ["python", "day1.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # send inputs exactly how the script expects them
    output, error = process.communicate(f"{city}\n{pet}\n")

    return {"result": output}
>>>>>>> 72f8e95250a075efe06866a340dc921d05036923
