from fastapi import FastAPI
from celery_worker import sumar, petition, petition_to_time

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "Mundo mundial"}

@app.get("/sumar/{x}/{y}")
async def sumar_task(x: int, y: int):
    result = sumar.apply_async((x, y))
    return {"task_id": result.id, "status": "task started"}

@app.get("/petition")
async def petition_task():
    result = petition.apply_async(())
    return {"task_id": result.id, "status": "task started"}

@app.post("/petition_to_time/{time_received}")
async def petition_task(time_received: int):
    result = petition_to_time.apply_async((time_received,))
    return {"task_id": result.id, "status": "task started"}
