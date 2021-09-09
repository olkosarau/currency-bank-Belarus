from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .models import CurrencyAuthUser, CurrencyUnAuthUser
from .serializers import CurrencyAuthUserSerializer, CurrencyUnAuthUserSerializer
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response


class AuthViewSet(GenericAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    @api_view(['GET'])
    def currency_bank_today(self, bank):
        if bank in (CurrencyAuthUser.ALPHABANK,CurrencyAuthUser.BELAGROPROMBANK, CurrencyAuthUser.BELARUSBANK):
            result = CurrencyAuthUser.objects.filter(company=bank).last()
            serializer = CurrencyAuthUserSerializer(result)
            return Response(serializer.data)
        else:
            return Response("Названия такого банка нет. Попробуйте ввести правильно!!!", 400)


class FilterDateView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self):
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date = self.request.query_params.get('date')
        if (company, date) is not None:
            return qs.filter(company__iexact=company, date__date=date)


class FilterDateIntervalView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self):
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        if (company, date_start, date_end) is not None:
            return qs.filter(date__range=[date_start, date_end], company__iexact=company)


class UnAuthViewSet(GenericAPIView):
    queryset = CurrencyUnAuthUser.objects.all()
    serializer_class = CurrencyUnAuthUserSerializer

    @api_view(['GET'])
    @permission_classes([AllowAny])
    def currency_bank_now(self, bank):
        if bank in (CurrencyUnAuthUser.ALPHABANK,CurrencyUnAuthUser.BELAGROPROMBANK, CurrencyUnAuthUser.BELARUSBANK):
            if bank == "alfabank":
                alfabankun()
            elif bank == "belagro":
                belagroun()
            elif bank == "belbank":
                belarusbankun()
            result = CurrencyUnAuthUser.objects.filter(company=bank).last()
            serializer = CurrencyUnAuthUserSerializer(result)
            return Response(serializer.data)
        else:
            return Response("Названия такого банка нет. Попробуйте ввести правильно!!!", 400)