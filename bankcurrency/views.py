from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import Auth, UnAuth
from .serializers import AuthSerializer, UnAuthSerializer
import bankcurrency
from bankcurrency.utils.auth import alfabank, belagro, belarusbank
from bankcurrency.utils.unauth import alfabankun, belagroun, belarusbankun
from rest_framework.views import Response


class AuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.Auth.objects.all()
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
    def data_date_current(self):
        tutors = Auth.objects.filter(date__day=19)
        tutor = AuthSerializer(tutors, many=True)
        return Response(tutor.data)

    @api_view(['GET'])
    def data_date_interval(self):
        tutors = Auth.objects.filter(date__day=18, company='АльфаБанк').filter(date__day=18)
        tutor = AuthSerializer(tutors, many=True)
        return Response(tutor.data)


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
