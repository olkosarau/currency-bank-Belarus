from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import Auth, UnAuth
from .serializers import AuthSerializer, UnAuthSerializer
import bankcurrency
from bankcurrency.curview.auth import alfabank, belagro, belarusbank
from bankcurrency.curview.unauth import alfabankun, belagroun, belarusbankun


"""Для авторизированных пользователей АльфаБанк"""


class AuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.Auth.objects.all()
    permissions_classes = permissions.IsAuthenticated
    serializer_class = AuthSerializer

    @api_view(['GET'])
    def alfa_bank(self):
        return alfabank(self)

    @api_view(['GET'])
    def bel_agro(self):
        return belagro(self)

    @api_view(['GET'])
    def belarus_bank(self):
        return belarusbank(self)


"""Для неавторизированных пользователей"""


class UnAuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.UnAuth.objects.all()
    permissions_classes = permissions.AllowAny
    serializer_class = UnAuthSerializer

    @api_view(['GET'])
    def alfa_bank(self):
        return alfabankun(self)

    @api_view(['GET'])
    def bel_agro(self):
        return belagroun(self)

    @api_view(['GET'])
    def belarus_bank(self):
        return belarusbankun(self)

    # def specific_date(self, request):
    #     """за определенную дату"""
    #     def post_date(self, request):
    #         date_input=request.post('Введите интересующую дату: ')
    #         data = date_input.ison()
    #         return Response(data)
    #
    #
    #
    # def current_moment(self):
    #     """за текущий момент"""
    #     cur_mom = AlfaBank.objects.filter(date=datetime.now().strftime("%d-%m-%Y %H:%M"), company='klkl')
    #     return cur_mom
    #
    # def time_interval(self):
    #     """за определенный промежуток времени"""
    #     cur_mo = AlfaBank.objects.exclude(date=datetime.now()).filter(date=datetime.date(2021, 8, 4))
    #     return cur_mo
