from datetime import date
from django.db.models import QuerySet
from rest_framework import permissions, generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .models import CurrencyAuthUser, CurrencyUnAuthUser
from .serializers import CurrencyAuthUserSerializer, CurrencyUnAuthUserSerializer
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response
from rest_framework.request import Request


class AuthViewSet(GenericAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get(self, request: Request, bank: str) -> Response:
        if bank in (CurrencyAuthUser.ALPHABANK, CurrencyAuthUser.BELAGROPROMBANK, CurrencyAuthUser.BELARUSBANK):
            result = CurrencyAuthUser.objects.filter(company=bank).last()
            serializer = CurrencyAuthUserSerializer(result)
            return Response(serializer.data)
        else:
            return Response("Названия такого банка нет. Попробуйте ввести правильно!!!", 404)


class FilterDateTodayView(GenericAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get(self, request: Request, banks: str) -> Response:
        current_date = date.today().day
        if banks in (CurrencyAuthUser.ALPHABANK, CurrencyAuthUser.BELAGROPROMBANK, CurrencyAuthUser.BELARUSBANK):
            result = CurrencyAuthUser.objects.filter(company=banks).filter(date__day=current_date).order_by('-id')
            serializer = CurrencyAuthUserSerializer(result, many=True)
            return Response(serializer.data)


class FilterDateView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self) -> QuerySet[CurrencyAuthUser]:
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date = self.request.query_params.get('date')
        if (company, date) is not None:
            return qs.filter(company__iexact=company, date__date=date).distinct('date__day')


class FilterDateIntervalView(generics.ListAPIView):
    queryset = CurrencyAuthUser.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = CurrencyAuthUserSerializer

    def get_queryset(self) -> QuerySet[CurrencyAuthUser]:
        qs = CurrencyAuthUser.objects.all()
        company = self.request.query_params.get('company')
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        if (company, date_start, date_end) is not None:
            return qs.filter(date__range=[date_start, date_end], company__iexact=company).distinct('date__day')


class UnAuthViewSet(GenericAPIView):
    queryset = CurrencyUnAuthUser.objects.all()
    serializer_class = CurrencyUnAuthUserSerializer
    permission_classes = [AllowAny]

    def get(self, request: Request, bank: str) -> Response:
        if bank in (CurrencyUnAuthUser.ALPHABANK, CurrencyUnAuthUser.BELAGROPROMBANK, CurrencyUnAuthUser.BELARUSBANK):
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
            return Response("Названия такого банка нет. Попробуйте ввести правильно!!!", 404)
