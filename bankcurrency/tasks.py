from .curview.task_selery import task_alfa, task_agro, task_bel
from devtest.celery import app


@app.task
def create_alphabank_currency():
    return task_alfa()


@app.task
def create_belagro_currency():
    return task_agro()


@app.task
def create_belarusbank_currency():
    return task_bel()
