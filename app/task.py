from celery import Celery

# Configura Celery para usar Redis
app = Celery('my_tasks', broker='redis://redis:6379/0')

@app.task
def get_example():
    import requests
    resultRequest = requests.get('https://w3schools.com/python/demopage.htm')
    print(resultRequest.text)

@app.task
def print_example():
    print("Comienza la serie de peticiones:")
    get_example.apply_async(countdown=2)