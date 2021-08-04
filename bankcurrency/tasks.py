from datetime import datetime

from celery import shared_task
from celery.worker.state import requests
from datetime import datetime
from .models import AlfaBank



@shared_task
def create_new_db():
    curr_req = requests.get(
        'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    data = curr_req.json()
    cur_rur_buy = data['rates'][3]['buyRate']
    cur_rur_sell = data['rates'][3]['sellRate']
    cur_eur_buy = data['rates'][4]['buyRate']
    cur_eur_sell = data['rates'][4]['sellRate']
    cur_usd_buy = data['rates'][5]['buyRate']
    cur_usd_sell = data['rates'][5]['sellRate']
    date_up = data['rates'][3]['date']
    date_time_obj = datetime.strptime(date_up, '%d.%m.%Y')

    cur_new = AlfaBank.objects.create(date=date_time_obj, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                      usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                      rur_sell=cur_rur_sell)
    cur_new.save()
    return cur_new
