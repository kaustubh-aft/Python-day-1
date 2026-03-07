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
