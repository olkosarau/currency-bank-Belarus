from rest_framework import permissions, generics
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import CurrencyAuthUser, CurrencyUnAuthUser
from .serializers import CurrencyAuthUserSerializer, CurrencyUnAuthUserSerializer
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response
from rest_framework.filters import SearchFilter


class AuthViewSet(GenericAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['date']

    @api_view(['GET'])
    def currency_alfa_bank_today(self):
        result = CurrencyAuthUser.objects.filter(company=CurrencyAuthUser.ALPHABANK).values().order_by('id').last()
        return Response(result)

    @api_view(['GET'])
    def currency_bel_agro_today(self):
        result = CurrencyAuthUser.objects.filter(company=CurrencyAuthUser.BELAGROPROMBANK).values().order_by(
            'id').last()
        return Response(result)

    @api_view(['GET'])
    def currensy_belarus_bank_today(self):
        result = CurrencyAuthUser.objects.filter(company=CurrencyAuthUser.BELARUSBANK).values().order_by('id').last()
        return Response(result)

class FilterDateView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    serializer_class = CurrencyAuthUserSerializer
    def get_queryset(self):
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date = self.request.query_params.get('date')
        return qs.filter(company__exact=company).values().filter(date__day=date)

class FilterDateIntervalView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self):
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        return qs.filter(date__range=[date_start,date_end],company__exact=company).values()

class UnAuthViewSet(GenericAPIView):
    queryset = CurrencyUnAuthUser.objects.all()
    permissions_classes = permissions.AllowAny
    serializer_class = CurrencyUnAuthUserSerializer

    @api_view(['GET'])
    def currency_alfa_bank_today(self):
        return alfabankun()

    @api_view(['GET'])
    def currency_bel_agro_today(self):
        return belagroun()

    @api_view(['GET'])
    def currensy_belarus_bank_today(self):
        return belarusbankun()
