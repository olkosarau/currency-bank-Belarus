import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devtest.settings')
app = Celery('devtest', broker='redis://redis:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'creating-cur_new': {
        'task': 'bankcurrency.tasks.create_alphabank_currency',
        'schedule': crontab(hour=1),
    }

}

app.conf.beat_schedule = {
    'creating-cur_new_1': {
        'task': 'bankcurrency.tasks.create_belagro_currency',
        'schedule': crontab(hour=1),
    }

}

app.conf.beat_schedule = {
    'creating-cur_new_2': {
        'task': 'bankcurrency.tasks.create_belarusbank_currency',
        'schedule': crontab(hour=1),
    }

}
