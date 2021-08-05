from rest_framework import permissions
from rest_framework.generics import GenericAPIView
import bankcurrency, requests
from .models import AlfaBank, Company, Date, AlfaBankUnAuth
from .serializers import (AlfaBankSerializer, AlfaBankUnAuthSerializer, CompanySerializer,
                          DateSerializer)
from rest_framework.views import APIView, Response, Request
from datetime import datetime
from celery.schedules import crontab
from bankcurrency.tasks import get
from devtest.celery import app


class AlfaBankViewSet(GenericAPIView):
    queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
    permissions_classes = (
        permissions.AllowAny,  # IsAuthenticated
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
        date_up = data['rates'][3]['date']
        date_time_obj = datetime.strptime(date_up, '%d.%m.%Y %H:%M:%S')

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


class DateViewSet(GenericAPIView):
    queryset = bankcurrency.models.Date.objects.all()
    permissions_classes = (
        permissions.AllowAny
    )
    serializer_class = DateSerializer

    def get(self, request, *args, **kwargs):
        date_req = requests.get('https://www.nbrb.by/api/exrates/rates[/{cur_id}]')
        data = date_req.json()
        date_buy = data['Rate'][Date]

        return Response(date_buy)


class AlfaBankUnAuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
    permissions_classes = (
        permissions.AllowAny
    )
    serializer_class = AlfaBankUnAuthSerializer

    def get(self, request):
        curr_req = requests.get(
            'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')  # Делаем запрос в АПИ
        data = curr_req.json()
        cur_rur = data['rates'][3]['buyRate']
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



app.conf.beat_schedule = {
    'creating-cur_new': {
        'task': 'bankcurrency.tasks.get',
        'schedule': crontab(hour=1),
    }

}