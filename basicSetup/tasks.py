# myapp/tasks.py
from celery import shared_task

@shared_task
def write_hello():
    with open('home.html', 'a') as f:
        f.write('hello\n')
