from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import Auth, UnAuth
from .serializers import AuthSerializer, UnAuthSerializer
from bankcurrency.utils.auth import alfabank, belagro, belarusbank
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response


class AuthViewSet(GenericAPIView):
    queryset = Auth.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = AuthSerializer

    @api_view(['GET'])
    def alfa_bank(self):
        return alfabank()

    @api_view(['GET'])
    def bel_agro(self):
        return belagro()

    @api_view(['GET'])
    def belarus_bank(self):
        return belarusbank()

    @api_view(['GET'])
    def alfa_query(self):
        queryset = Auth.objects.all()
        company = self.request.query_params.get('company')
        date = self.request.query_params.get('date')
        if company is not None:
            if date is not None:
                queryset = queryset.filter(purchaser__date=date)

        return queryset

    @api_view(['GET'])
    def data_date_interval(self):
        queryset = Auth.objects.all()
        company = self.request.query_params.get('company')
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        if company is not None:
            if date_start is not None:
                if date_end is not None:
                    queryset = queryset.filter(date__range=[date_start, date_end])
        return queryset


class UnAuthViewSet(GenericAPIView):
    queryset = UnAuth.objects.all()
    permissions_classes = permissions.AllowAny
    serializer_class = UnAuthSerializer

    @api_view(['GET'])
    def alfa_bank(self):
        return alfabankun()

    @api_view(['GET'])
    def bel_agro(self):
        return belagroun()

    @api_view(['GET'])
    def belarus_bank(self):
        return belarusbankun()
