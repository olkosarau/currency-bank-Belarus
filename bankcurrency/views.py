from rest_framework import permissions
from rest_framework.generics import GenericAPIView
import bankcurrency, requests
from .models import AlfaBank
from .serializers import (AlfaBankSerializer, AlfaBankUnAuthSerializer, BelApbSerializer, BelApbUnAuthSerializer)
from rest_framework.views import Response
from datetime import datetime
from celery.schedules import crontab
from devtest.celery import app

"""Для авторизированных пользователей"""


class AlfaBankViewSet(GenericAPIView):
    queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
    # permissions_classes = (
    #     permissions.IsAuthenticated
    # )
    authentication_classes = [permissions.IsAuthenticated, ]
    serializer_class = AlfaBankSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')  # Делаем запрос в АПИ
        data = curr_req.json()
        cur_rur_buy = ((data['rates'][3]['buyRate']) / 100)
        cur_rur_sell = ((data['rates'][3]['sellRate']) / 100)
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
        response = Response({'usd_buy': cur_usd_buy,
                             'usd_sell': cur_usd_sell,
                             'eur_buy': cur_eur_buy,
                             'eur_sell': cur_eur_sell,
                             'rur_buy': cur_rur_buy,
                             'rur_sell': cur_rur_sell,
                             'date': date_up
                             })
        return response


"""Для не авторизированных пользователей"""


class AlfaBankUnAuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
    permissions_classes = (
        permissions.AllowAny
    )
    serializer_class = AlfaBankUnAuthSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
        data = curr_req.json()
        cur_rur = ((data['rates'][3]['buyRate']) / 100)
        cur_eur = data['rates'][4]['buyRate']
        cur_usd = data['rates'][5]['buyRate']
        title = data['rates'][3]['date']
        response = Response({'usd': cur_usd,
                             'eur': cur_eur,
                             'rur': cur_rur,
                             'date': title
                             })

        return response

    def post(self, *args):
        pass


"""Задача в CELERY на каждый час"""
app.conf.beat_schedule = {
    'creating-cur_new': {
        'task': 'bankcurrency.tasks.get',
        'schedule': crontab(hour='*/1'),
    }

}


"""Информация по курсам валют за определенные сроки"""
queryset = bankcurrency.models.AlfaBank.objects.all()


def specific_date():
    """за определенную дату"""
    cur_m = AlfaBank.objects.filter(date='2021.08.06')
    return cur_m


def current_moment():
    """за текущий момент"""
    cur_mom = AlfaBank.objects.filter(date=datetime.date.today)
    return cur_mom


def time_interval():
    """за определенный промежуток времени"""
    cur_mo = AlfaBank.objects.exclude(date=datetime.date.today()).filter(date=datetime.date(2021, 8, 4))
    return cur_mo



