from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import Auth, UnAuth
from .serializers import AuthSerializer, UnAuthSerializer
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response


class AuthViewSet(GenericAPIView):
    queryset = Auth.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = AuthSerializer

    @api_view(['GET'])
    def currency_alfa_bank_today(self):
        result = Auth.objects.filter(company=Auth.ALPHABANK).values().order_by('id').last()
        return Response(result)

    @api_view(['GET'])
    def currency_bel_agro_today(self):
        result = Auth.objects.filter(company=Auth.BELAGROPROMBANK).values().order_by('id').last()
        return Response(result)

    @api_view(['GET'])
    def currensy_belarus_bank_today(self):
        result = Auth.objects.filter(company=Auth.BELARUSBANK).values().order_by('id').last()
        return Response(result)

    @api_view(['GET'])
    def date_get_queryset(self):
        queryset = Auth.objects.get()
        date = self.request.query_params.get['date']

        if date:
            queryset = queryset.filter(date_id=date)

        return queryset


    def interval_get_queryset (self):
        queryset = Auth.objects.get()
        date_start = self.request.query_params.get['date_start']
        date_end = self.request.query_params.get['date_end']
        if date_start and date_end :
            queryset = queryset.filter(date__range = [date_start, date_end])

        return queryset



class UnAuthViewSet(GenericAPIView):
    queryset = UnAuth.objects.all()
    permissions_classes = permissions.AllowAny
    serializer_class = UnAuthSerializer

    @api_view(['GET'])
    def currency_alfa_bank_today(self):
        return alfabankun()

    @api_view(['GET'])
    def currency_bel_agro_today(self):
        return belagroun()

    @api_view(['GET'])
    def currensy_belarus_bank_today(self):
        return belarusbankun()
