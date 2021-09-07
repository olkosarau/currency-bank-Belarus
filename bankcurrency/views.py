from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .models import CurrencyAuthUser, CurrencyUnAuthUser
from .serializers import CurrencyAuthUserSerializer, CurrencyUnAuthUserSerializer
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response, APIView


class AuthViewSet(GenericAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def replace(bank):
        if bank == 'alfabank':
            return 'АльфаБанк'
        elif bank == 'belagro':
            return 'БелАгроПромБанк'
        elif bank == 'belbank':
            return 'БеларусБанк'

    @api_view(['GET'])
    def currency_bank_today(self, bank):
        rez = AuthViewSet.replace(bank)
        if CurrencyAuthUser.objects.filter(company=rez).exists():
            result = CurrencyAuthUser.objects.filter(company="{0}".format(rez)).values().last()
            return Response(result)
        else:
            return Response("Названия такого банка нет. Попробуйте ввести правильно!!!", 204)


class FilterDateView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self):
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date = self.request.query_params.get('date')
        return qs.filter(company__iexact=company).values().filter(date__date=date)


class FilterDateIntervalView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self):
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        return qs.filter(date__range=[date_start, date_end], company__iexact=company).values()


class UnAuthViewSet(APIView):
    queryset = CurrencyUnAuthUser.objects.all()
    serializer_class = CurrencyUnAuthUserSerializer

    @api_view(['GET'])
    @permission_classes([AllowAny])
    def currency_bank_today(self, bank):
        rez = AuthViewSet.replace(bank)
        if CurrencyAuthUser.objects.filter(company=rez).exists():
            if rez == "АльфаБанк":
                alfabankun()
            elif rez == "БелАгроПромБанк":
                belagroun()
            elif rez == "БеларусБанк":
                belarusbankun()
            result = CurrencyUnAuthUser.objects.filter(company="{0}".format(rez)).values().last()
            return Response(result)
        else:
            return Response("Банка нет", 204)
