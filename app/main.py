from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from fastapi import FastAPI
import requests

app = FastAPI()
scheduler = BackgroundScheduler()
sched = BlockingScheduler()

def getExample():
    resultRequest = requests.get('https://w3schools.com/python/demopage.htm')
    print(resultRequest.text)

def printExample():
    print("Comienza la serie de peticiones:")
    other_scheduler()

def other_scheduler():
    scheduler.add_job(getExample, 'interval', seconds=2)
    scheduler.start()

@app.on_event("startup")
def start_scheduler():
    # Date AAAA, MM, DD, hh, mm, ss
    run_date = datetime(2025, 3, 12, 13, 48, 2)
    sched.add_job(printExample, 'date', run_date=run_date)
    sched.start()

@app.get("/")
def read_root():
    return {"Hello": "World"}