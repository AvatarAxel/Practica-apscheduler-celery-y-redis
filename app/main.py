from fastapi import FastAPI
from celery_worker import sumar

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "¡Hola, FastAPI y Celery!"}

@app.get("/sumar/{x}/{y}")
async def sumar_task(x: int, y: int):
    result = sumar.apply_async((x, y))
    return {"task_id": result.id, "status": "task started"}