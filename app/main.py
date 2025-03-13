from fastapi import FastAPI
from datetime import datetime
from app.task import print_example

app = FastAPI()

@app.on_event("startup")
def start_scheduler():
    run_date = datetime(2025, 3, 12, 13, 48, 2)
    print_example.apply_async(eta=run_date)

@app.get("/")
def read_root():
    return {"Hello": "World"}