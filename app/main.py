from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult
from datetime import datetime
from app.task import print_example, task_de_prueba, app as celery_app
import pytz

app = FastAPI()

@app.on_event("startup")
def start_scheduler():
    cdmx_tz = pytz.timezone("America/Mexico_City")
    run_date = datetime(2025, 3, 12, 14, 15, 0, tzinfo=cdmx_tz)
    print("Mi hora que configuro:", run_date)
    print("La hora actual en mi zona horaria:", datetime.now(cdmx_tz))
    print("Tarea programada: ", print_example.apply_async(eta=run_date))
    print("Tarea de prueba: ", task_de_prueba.apply_async())

@app.get("/")
def read_root():
    print("uwu")
    return {"Onichan": "uwu"}

@app.get("/task-result/{task_id}")
def get_task_result(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.ready():
        return {"task_id": task_id, "status": task_result.status, "result": task_result.result}
    else:
        return {"task_id": task_id, "status": task_result.status}
