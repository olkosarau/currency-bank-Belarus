from rest_framework import permissions
from rest_framework.generics import GenericAPIView
import bankcurrency, requests
from .models import AlfaBank, Company, Date, AlfaBankUnAuth
from .serializers import (AlfaBankSerializer, AlfaBankUnAuthSerializer, CompanySerializer,
                          DateSerializer)
from rest_framework.views import APIView, Response, Request


class AlfaBankViewSet(GenericAPIView):
    queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
    permissions_classes = (
        permissions.AllowAny,  # IsAuthenticated
    )
    # authentication_classes = [permissions.IsAuthenticated, ]
    serializer_class = AlfaBankSerializer

    def get(self, request):
        # if request.user.is_authenticated:   # Проверка на аторизацию
        curr_req = requests.get(
            'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')  # Делаем запрос в АПИ
        data = curr_req.json()
        cur_rur_buy = data['rates'][3]['buyRate']
        cur_rur_sell = data['rates'][3]['sellRate']
        cur_eur_buy = data['rates'][5]['buyRate']
        cur_eur_sell = data['rates'][5]['sellRate']
        cur_usd_buy = data['rates'][4]['buyRate']
        cur_usd_sell = data['rates'][4]['sellRate']
        date = data['rates'][3]['date']
        date_up = date.isoformat()
        AlfaBank.objects.create(date=date_up, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                rur_sell=cur_rur_sell)
        response = Response({'usd_buy': cur_usd_buy,
                             'usd_sell': cur_usd_sell,
                             'eur_buy': cur_eur_buy,
                             'eur_sell': cur_eur_sell,
                             'rur_buy_buy': cur_rur_buy,
                             'rur_buy_sell': cur_rur_sell,
                             'date': date_up
                             })
        return response

    def post(self, *args):
        pass

    @classmethod
    def get_extra_actions(cls):
        return []


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

# def my_login(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#
#     else:
#         form = UserRegisterForm()
#                   # Вход не был выполнен
#     context = {'form':form}
#     return render(request, 'register.html', context)
