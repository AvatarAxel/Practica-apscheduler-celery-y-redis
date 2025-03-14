import requests
from celery import Celery
import time

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def fetch_url_task():
    while True:
        try:
            result = requests.get('https://w3schools.com/python/demopage.htm')
            print(result.text)
        except Exception as e:
            print(f"Error al hacer la solicitud: {e}")
        time.sleep(5)
