from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import CurrencyAuthUser, CurrencyUnAuthUser
from .serializers import CurrencyAuthUserSerializer, CurrencyUnAuthUserSerializer
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response


class AuthViewSet(GenericAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

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

    @api_view(['GET'])
    def date_get_queryset(self):
        queryset = CurrencyAuthUser.objects.get()
        date = self.request.query_params.get['date']

        if date:
            queryset = queryset.filter(date_id=date)

        return queryset

    def interval_get_queryset(self):
        queryset = CurrencyAuthUser.objects.get()
        date_start = self.request.query_params.get['date_start']
        date_end = self.request.query_params.get['date_end']
        if date_start and date_end:
            queryset = queryset.filter(date__range=[date_start, date_end])

        return queryset


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
