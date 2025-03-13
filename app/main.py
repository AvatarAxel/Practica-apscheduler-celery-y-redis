from fastapi import FastAPI
from datetime import datetime
from app.task import print_example

app = FastAPI()

@app.on_event("startup")
def start_scheduler():
    # Date YYYY/MM/DD hh/mm/ss
    run_date = datetime(2025, 3, 12, 11, 5, 1)
    print("Tii")
    print(datetime.now())
    print_example.apply_async(eta=run_date)

@app.get("/")
def read_root():
    print("uwu")
    return {"Onichan": "uwu, yiyi"}