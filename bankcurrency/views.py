from rest_framework import permissions
from rest_framework.generics import GenericAPIView
import bankcurrency, requests
from .models import AlfaBank, BelApb, BelBank
from .serializers import (AlfaBankSerializer, AlfaBankUnAuthSerializer, BelApbSerializer, BelApbUnAuthSerializer,
                          BelBankSerializer, BelBankUnAuthSerializer)
from rest_framework.views import Response, APIView
from datetime import datetime
from celery.schedules import crontab
from devtest.celery import app
from django.utils import timezone
import requests
import xml.etree.ElementTree as et

"""Для авторизированных пользователей АльфаБанк"""


class AlfaBankViewSet(GenericAPIView):
    queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
    permissions_classes = (
        permissions.AllowAny
    )
    # authentication_classes = [permissions.IsAuthenticated, ]
    serializer_class = AlfaBankSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')  # Делаем запрос в АПИ
        data = curr_req.json()
        cur_rur_buy = data['rates'][3]['buyRate']
        cur_rur_sell = data['rates'][3]['sellRate']
        cur_eur_buy = data['rates'][4]['buyRate']
        cur_eur_sell = data['rates'][4]['sellRate']
        cur_usd_buy = data['rates'][5]['buyRate']
        cur_usd_sell = data['rates'][5]['sellRate']
        # date_up = data['rates'][3]['date']
        date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

        cur_new = AlfaBank.objects.create(eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                          usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                          rur_sell=cur_rur_sell)
        cur_new.save()
        response = Response({'usd_buy': cur_usd_buy,
                             'usd_sell': cur_usd_sell,
                             'eur_buy': cur_eur_buy,
                             'eur_sell': cur_eur_sell,
                             'rur_buy': cur_rur_buy,
                             'rur_sell': cur_rur_sell,
                             'date': date_time_obj
                             })
        return response


    def specific_date(self):
        """за определенную дату"""
        cur_m = AlfaBank.objects.filter(date='2021.08.06')
        return cur_m

    def current_moment(self):
        """за текущий момент"""
        cur_mom = AlfaBank.objects.filter(date=datetime.now().strftime("%d-%m-%Y %H:%M"))
        return cur_mom

    def time_interval(self):
        """за определенный промежуток времени"""
        cur_mo = AlfaBank.objects.exclude(date=datetime.now()).filter(date=datetime.date(2021, 8, 4))
        return cur_mo

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


"""Для авторизированных пользователей БелАгроПромБанк"""


class BelApbViewSet(APIView):
    queryset = bankcurrency.models.BelApb.objects.all()
    permissions_classes = (
        permissions.AllowAny
    )
    # authentication_classes = [permissions.IsAuthenticated, ]
    serializer_class = BelApbSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://belapb.by/ExCardsDaily.php?')
        print(curr_req.status_code)
        tree = et.ElementTree(et.fromstring(curr_req.text))  # .text возвращает содержимое ответа в формате Unicode.
        root = tree.getroot()

        s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        s_eur_buy = root[0][3].text
        s_eur_sell = root[0][4].text
        s_usd_buy = root[1][3].text
        s_usd_sell = root[1][4].text
        s_rur_buy = root[2][3].text
        s_rur_sell = root[2][4].text

        cur_new = BelApb.objects.create(eur_buy=s_eur_buy, eur_sell=s_eur_sell,
                                        usd_buy=s_usd_buy, usd_sell=s_usd_sell, rur_buy=s_rur_buy,
                                        rur_sell=s_rur_sell)
        cur_new.save()
        response = Response({'usd_buy': s_usd_buy,
                             'usd_sell': s_usd_sell,
                             'eur_buy': s_eur_buy,
                             'eur_sell': s_eur_sell,
                             'rur_buy': s_rur_buy,
                             'rur_sell': s_rur_sell,
                             'date': s_date
                             })
        return response

    def specific_date(self):
        """за определенную дату"""
        cur_m = BelApb.objects.filter(date='2021.08.06')
        return cur_m

    def current_moment(self):
        """за текущий момент"""
        cur_mom = BelApb.objects.filter(date=datetime.now().strftime("%d-%m-%Y %H:%M"))
        return cur_mom

    def time_interval(self):
        """за определенный промежуток времени"""
        cur_mo = BelApb.objects.exclude(date=datetime.now()).filter(date=datetime.date(2021, 8, 4))
        return cur_mo


"""Для неавторизированных пользователей"""


class BelApbUnAuthViewSet(APIView):
    queryset = bankcurrency.models.BelApb.objects.all()
    permissions_classes = (
        permissions.AllowAny
    )
    # authentication_classes = [permissions.IsAuthenticated, ]
    serializer_class = BelApbSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://belapb.by/ExCardsDaily.php?')
        print(curr_req.status_code)
        tree = et.ElementTree(et.fromstring(curr_req.text))  # .text возвращает содержимое ответа в формате Unicode.
        root = tree.getroot()

        s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        s_eur_buy = root[0][3].text
        s_eur_sell = root[0][4].text
        s_usd_buy = root[1][3].text
        s_usd_sell = root[1][4].text
        s_rur_buy = root[2][3].text
        s_rur_sell = root[2][4].text

        response = Response({'usd_buy': s_usd_buy,
                             'usd_sell': s_usd_sell,
                             'eur_buy': s_eur_buy,
                             'eur_sell': s_eur_sell,
                             'rur_buy': s_rur_buy,
                             'rur_sell': s_rur_sell,
                             'date': s_date
                             })
        return response


"""Для авторизированных пользователей <БеларусБанк>"""


class BelBankViewSet(GenericAPIView):
    queryset = bankcurrency.models.BelBank.objects.all()
    permissions_classes = (
        permissions.AllowAny
    )
    # authentication_classes = [permissions.IsAuthenticated, ]
    serializer_class = BelBankSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://belarusbank.by/api/kursExchange?city=Минск')
        data = curr_req.json()
        cur_rur_buy = data[0]['RUB_in']
        cur_rur_sell = data[0]['RUB_out']
        cur_eur_buy = data[0]['EUR_in']
        cur_eur_sell = data[0]['EUR_out']
        cur_usd_buy = data[0]['USD_in']
        cur_usd_sell = data[0]['USD_out']

        date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

        cur_new = BelBank.objects.create(eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                         usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                         rur_sell=cur_rur_sell)
        cur_new.save()
        response = Response({'usd_buy': cur_usd_buy,
                             'usd_sell': cur_usd_sell,
                             'eur_buy': cur_eur_buy,
                             'eur_sell': cur_eur_sell,
                             'rur_buy': cur_rur_buy,
                             'rur_sell': cur_rur_sell,
                             'date': date_time_obj
                             })
        return response


    def specific_date(self):
        """за определенную дату"""
        cur_m = BelBank.objects.filter(date='2021.08.06')
        return cur_m

    def current_moment(self):
        """за текущий момент"""
        cur_mom = BelBank.objects.filter(date=datetime.now().strftime("%d-%m-%Y %H:%M"))
        return cur_mom

    def time_interval(self):
        """за определенный промежуток времени"""
        cur_mo = BelBank.objects.exclude(date=datetime.now()).filter(date=datetime.date(2021, 8, 4))
        return cur_mo

"""Для не авторизированных пользователей"""


class BelBankUnAuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.BelBank.objects.all()  # это наши объекты в базе данных
    permissions_classes = (
        permissions.AllowAny
    )
    serializer_class = BelBankUnAuthSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://belarusbank.by/api/kursExchange?city=Минск')
        data = curr_req.json()
        cur_rur_buy = data[0]['RUB_in']
        cur_rur_sell = data[0]['RUB_out']
        cur_eur_buy = data[0]['EUR_in']
        cur_eur_sell = data[0]['EUR_out']
        cur_usd_buy = data[0]['USD_in']
        cur_usd_sell = data[0]['USD_out']
        date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

        response = Response({'usd_buy': cur_usd_buy,
                             'usd_sell': cur_usd_sell,
                             'eur_buy': cur_eur_buy,
                             'eur_sell': cur_eur_sell,
                             'rur_buy': cur_rur_buy,
                             'rur_sell': cur_rur_sell,
                             'date': date_time_obj
                             })

        return response

    def post(self, *args):
        pass






"""Задача в CELERY на каждый час"""
app.conf.beat_schedule = {
    'creating-cur_new': {
        'task': 'bankcurrency.tasks.get',
        'schedule': crontab(minute='*/59', hour='6-19', day_of_week='mon-sun'),
    }

}

