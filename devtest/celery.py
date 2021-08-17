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
        'task': 'bankcurrency.tasks.create_alphabank_currency',
        'schedule': crontab(1),
    }

}

app.conf.beat_schedule = {
    'creating-cur_new_1': {
        'task': 'bankcurrency.tasks.create_belagro_currency',
        'schedule': crontab(2),
    }

}

app.conf.beat_schedule = {
    'creating-cur_new_2': {
        'task': 'bankcurrency.tasks.create_belarusbank_currency',
        'schedule': crontab(3),
    }

}