from celery import Celery
import requests

celery_app = Celery('worker', broker='redis://localhost:6379/0')

@celery_app.task
def sumar(x, y):
    return x + y

@celery_app.task
def petition():
    resultRequest = requests.get('https://w3schools.com/python/demopage.htm')
    return resultRequest.text

@celery_app.task
def petition_to_time(time_received):
    resultRequest = requests.get('https://w3schools.com/python/demopage.htm')
    return resultRequest.text