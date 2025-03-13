from celery import Celery
import requests

app = Celery('my_tasks', 
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0')

@app.task
def get_example():
    resultRequest = requests.get('https://w3schools.com/python/demopage.htm')
    return resultRequest.text

@app.task
def print_example():
    print("Comienza la serie de peticiones:")
    get_example.apply_async(countdown=2)

@app.task
def task_de_prueba():
    resultRequest = requests.get('https://w3schools.com/python/demopage.htm')
    return resultRequest.text