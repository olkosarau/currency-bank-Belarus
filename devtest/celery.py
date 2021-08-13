import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devtest.settings')
app = Celery('devtest', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

"""Задача в CELERY на каждый час"""
"""1. Командой docker-compose up запустить REDIS"""
"""2. Командой celery -A devtest worker -l INFO запустить CELERY"""
app.conf.beat_schedule = {
    'creating-cur_new': {
        'task': 'bankcurrency.tasks.get_db',
        'schedule': crontab(10),
    }

}

app.conf.beat_schedule = {
    'creating-cur_new_1': {
        'task': 'bankcurrency.tasks.get_db_1',
        'schedule': crontab(40),
    }

}

app.conf.beat_schedule = {
    'creating-cur_new_2': {
        'task': 'bankcurrency.tasks.get_db_2',
        'schedule': crontab(59),
    }

}