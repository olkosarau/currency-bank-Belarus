from rest_framework import permissions, generics
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import CurrencyAuthUser, CurrencyUnAuthUser
from .serializers import CurrencyAuthUserSerializer, CurrencyUnAuthUserSerializer
from bankcurrency.utils.unauth import alfabankun
from rest_framework.views import Response


class AuthViewSet(GenericAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    @api_view(['GET'])
    def currency_bank_today(self, bank):
        if CurrencyAuthUser.objects.filter(company=bank).exists():
            result = CurrencyAuthUser.objects.filter(company="{0}".format(bank)).values().last()
            return Response(result)
        else:
            return Response("Названия такого банка нет. Попробуйте ввести правильно!!!")


class FilterDateTodayView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self):
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date_today = self.request.query_params.get('date_today')
        return qs.filter(company__iexact=company).values().filter(date__date=date_today)


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


class UnAuthViewSet(GenericAPIView):
    queryset = CurrencyUnAuthUser.objects.all()
    permissions_classes = permissions.AllowAny
    serializer_class = CurrencyUnAuthUserSerializer

    @api_view(['GET'])
    def currency_bank_today(self, bank):
        if CurrencyAuthUser.objects.filter(company=bank).exists():
            alfabankun()
            result = CurrencyUnAuthUser.objects.filter(company="{0}".format(bank)).values().last()
            return Response(result)
        else:
            return Response("Банка нет")
