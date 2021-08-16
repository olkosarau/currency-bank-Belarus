from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .models import Auth, UnAuth
from .serializers import AuthSerializer, UnAuthSerializer
from rest_framework.views import Response
from datetime import datetime
import requests
import xml.etree.ElementTree as et
import bankcurrency


"""Для авторизированных пользователей АльфаБанк"""


class AuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.Auth.objects.all()
    permissions_classes = (permissions.IsAuthenticated)
    serializer_class = AuthSerializer

    @api_view(['GET'])
    def alfa_bank(self):
        curr_req = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
        data = curr_req.json()
        cur_rur_sell = data['rates'][3]['buyRate']
        cur_rur_buy = data['rates'][3]['sellRate']
        cur_eur_sell = data['rates'][0]['buyRate']
        cur_eur_buy = data['rates'][0]['sellRate']
        cur_usd_sell = data['rates'][4]['buyRate']
        cur_usd_buy = data['rates'][4]['sellRate']
        date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

        cur_new = Auth.objects.create(company=Auth.ALPHABANK, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                      usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                      rur_sell=cur_rur_sell)
        cur_new.save()
        response = Response({'company': Auth.ALPHABANK,
                             'usd_buy': cur_usd_buy,
                             'usd_sell': cur_usd_sell,
                             'eur_buy': cur_eur_buy,
                             'eur_sell': cur_eur_sell,
                             'rur_buy': cur_rur_buy,
                             'rur_sell': cur_rur_sell,
                             'date': date_time_obj
                             })
        return response

    @api_view(['GET'])
    def bel_agro(self):
        curr_req = requests.get('https://belapb.by/ExCardsDaily.php?')
        print(curr_req.status_code)
        tree = et.ElementTree(et.fromstring(curr_req.text))
        root = tree.getroot()

        s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        s_eur_buy = root[1][3].text
        s_eur_sell = root[1][4].text
        s_usd_buy = root[0][3].text
        s_usd_sell = root[0][4].text
        s_rur_buy = root[2][3].text
        s_rur_sell = root[2][4].text

        cur_new = Auth.objects.create(company=Auth.BELAGROPROMBANK, eur_buy=s_eur_buy, eur_sell=s_eur_sell,
                                      usd_buy=s_usd_buy, usd_sell=s_usd_sell, rur_buy=s_rur_buy,
                                      rur_sell=s_rur_sell)
        cur_new.save()
        response = Response({'company': Auth.BELAGROPROMBANK,
                             'usd_buy': s_usd_buy,
                             'usd_sell': s_usd_sell,
                             'eur_buy': s_eur_buy,
                             'eur_sell': s_eur_sell,
                             'rur_buy': s_rur_buy,
                             'rur_sell': s_rur_sell,
                             'date': s_date
                              })
        return response

    @api_view(['GET'])
    def belarus_bank(self):
        curr_req = requests.get('https://belarusbank.by/api/kursExchange?city=Минск')
        data = curr_req.json()
        cur_rur_buy = data[0]['RUB_in']
        cur_rur_sell = data[0]['RUB_out']
        cur_eur_buy = data[0]['EUR_in']
        cur_eur_sell = data[0]['EUR_out']
        cur_usd_buy = data[0]['USD_in']
        cur_usd_sell = data[0]['USD_out']

        date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

        cur_new = Auth.objects.create(company=Auth.BELARUSBANK, eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
                                      usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
                                      rur_sell=cur_rur_sell)
        cur_new.save()
        response = Response({'company': Auth.BELARUSBANK,
                             'usd_buy': cur_usd_buy,
                             'usd_sell': cur_usd_sell,
                             'eur_buy': cur_eur_buy,
                             'eur_sell': cur_eur_sell,
                             'rur_buy': cur_rur_buy,
                             'rur_sell': cur_rur_sell,
                             'date': date_time_obj
                             })
        return response

    """Для неавторизированных пользователей"""


class UnAuthViewSet(GenericAPIView):
    queryset = bankcurrency.models.UnAuth.objects.all()
    permissions_classes = (permissions.AllowAny)
    serializer_class = UnAuthSerializer

    @api_view(['GET'])
    def alfa_bank(self):
        curr_req = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
        data = curr_req.json()
        cur_rur_sell = data['rates'][3]['buyRate']
        cur_eur_sell = data['rates'][0]['buyRate']
        cur_usd_sell = data['rates'][4]['buyRate']
        date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

        cur_new = UnAuth.objects.create(company=UnAuth.ALPHABANK, eur=cur_eur_sell,
                                        usd=cur_usd_sell, rur=cur_rur_sell)
        cur_new.save()
        return Response({'company': UnAuth.ALPHABANK,
                         'usd': cur_usd_sell,
                         'eur': cur_eur_sell,
                         'rur': cur_rur_sell,
                         'date': date_time_obj
                         })

    @api_view(['GET'])
    def bel_agro(self):
        curr_req = requests.get('https://belapb.by/ExCardsDaily.php?')
        print(curr_req.status_code)
        tree = et.ElementTree(et.fromstring(curr_req.text))
        root = tree.getroot()

        s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        s_eur_sell = root[1][4].text
        s_usd_sell = root[0][4].text
        s_rur_sell = root[2][4].text

        cur_new = UnAuth.objects.create(company=UnAuth.BELAGROPROMBANK, eur=s_eur_sell,
                                        usd=s_usd_sell, rur=s_rur_sell)
        cur_new.save()
        return Response({'company': UnAuth.BELAGROPROMBANK,
                         'usd': s_usd_sell,
                         'eur': s_eur_sell,
                         'rur': s_rur_sell,
                         'date': s_date
                         })

    @api_view(['GET'])
    def belarus_bank(self):
        curr_req = requests.get('https://belarusbank.by/api/kursExchange?city=Минск')
        data = curr_req.json()
        cur_rur_sell = data[0]['RUB_out']
        cur_eur_sell = data[0]['EUR_out']
        cur_usd_sell = data[0]['USD_out']

        date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")

        cur_new = UnAuth.objects.create(company=UnAuth.BELARUSBANK, eur=cur_eur_sell,
                                        usd=cur_usd_sell, rur=cur_rur_sell)
        cur_new.save()
        return Response({'company': UnAuth.BELARUSBANK,
                         'usd': cur_usd_sell,
                         'eur': cur_eur_sell,
                         'rur': cur_rur_sell,
                         'date': date_time_obj
                         })

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
    #     cur_mom = AlfaBank.objects.filter(date=datetime.now().strftime("%d-%m-%Y %H:%M"))
    #     return cur_mom
    #
    # def time_interval(self):
    #     """за определенный промежуток времени"""
    #     cur_mo = AlfaBank.objects.exclude(date=datetime.now()).filter(date=datetime.date(2021, 8, 4))
    #     return cur_mo

#
# """Для неавторизированных пользователей"""
#
#
# class AlfaBankUnAuthViewSet(GenericAPIView):
#     queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
#     permissions_classes = (
#         permissions.AllowAny
#     )
#     serializer_class = AlfaBankUnAuthSerializer
#
#     def get(self, request):
#         curr_req = requests.get(
#             'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
#         data = curr_req.json()
#         cur_rur = ((data['rates'][3]['buyRate']) / 100)
#         cur_eur = data['rates'][4]['buyRate']
#         cur_usd = data['rates'][5]['buyRate']
#         title = data['rates'][3]['date']
#         response = Response({'usd': cur_usd,
#                              'eur': cur_eur,
#                              'rur': cur_rur,
#                              'date': title
#                              })
#
#         return response
#
#     def post(self, *args):
#         pass
#
#
# """Для авторизированных пользователей БелАгроПромБанк"""
#
#
# class BelApbViewSet(GenericAPIView):
#     queryset = bankcurrency.models.BelApb.objects.all()
#     permissions_classes = (
#         permissions.IsAuthenticated
#     )
#     serializer_class = BelApbSerializer
#
#     def get(self, request):
#         if request.user.is_authenticated:
#             curr_req = requests.get(
#                 'https://belapb.by/ExCardsDaily.php?')
#             print(curr_req.status_code)
#             tree = et.ElementTree(et.fromstring(curr_req.text))  # .text возвращает содержимое ответа в формате Unicode.
#             root = tree.getroot()
#
#             s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
#             s_eur_buy = root[1][3].text
#             s_eur_sell = root[1][4].text
#             s_usd_buy = root[0][3].text
#             s_usd_sell = root[0][4].text
#             s_rur_buy = root[2][3].text
#             s_rur_sell = root[2][4].text
#
#             cur_new = BelApb.objects.create(eur_buy=s_eur_buy, eur_sell=s_eur_sell,
#                                             usd_buy=s_usd_buy, usd_sell=s_usd_sell, rur_buy=s_rur_buy,
#                                             rur_sell=s_rur_sell)
#             cur_new.save()
#             response = Response({'usd_buy': s_usd_buy,
#                                  'usd_sell': s_usd_sell,
#                                  'eur_buy': s_eur_buy,
#                                  'eur_sell': s_eur_sell,
#                                  'rur_buy': s_rur_buy,
#                                  'rur_sell': s_rur_sell,
#                                  'date': s_date
#                                  })
#             return response
#         else:
#             return redirect('/unauchBAB')
#
#     def specific_date(self):
#         """за определенную дату"""
#         cur_m = BelApb.objects.filter(date='2021.08.06')
#         return cur_m
#
#     def current_moment(self):
#         """за текущий момент"""
#         cur_mom = BelApb.objects.filter(date=datetime.now().strftime("%d-%m-%Y %H:%M"))
#         return cur_mom
#
#     def time_interval(self):
#         """за определенный промежуток времени"""
#         cur_mo = BelApb.objects.exclude(date=datetime.now()).filter(date=datetime.date(2021, 8, 4))
#         return cur_mo
#
#
# """Для неавторизированных пользователей"""
#
#
# class BelApbUnAuthViewSet(GenericAPIView):
#     queryset = bankcurrency.models.BelApb.objects.all()
#     permissions_classes = (
#         permissions.AllowAny
#     )
#     # authentication_classes = [permissions.IsAuthenticated, ]
#     serializer_class = BelApbUnAuthSerializer
#
#     def get(self, request):
#         curr_req = requests.get(
#             'https://belapb.by/ExCardsDaily.php?')
#         print(curr_req.status_code)
#         tree = et.ElementTree(et.fromstring(curr_req.text))  # .text возвращает содержимое ответа в формате Unicode.
#         root = tree.getroot()
#
#         s_date = datetime.now().strftime("%d-%m-%Y %H:%M")
#         s_eur_buy = root[1][3].text
#         s_eur_sell = root[1][4].text
#         s_usd_buy = root[0][3].text
#         s_usd_sell = root[0][4].text
#         s_rur_buy = root[2][3].text
#         s_rur_sell = root[2][4].text
#
#         response = Response({'usd_buy': s_usd_buy,
#                              'usd_sell': s_usd_sell,
#                              'eur_buy': s_eur_buy,
#                              'eur_sell': s_eur_sell,
#                              'rur_buy': s_rur_buy,
#                              'rur_sell': s_rur_sell,
#                              'date': s_date
#                              })
#         return response
#
#
# """Для авторизированных пользователей <БеларусБанк>"""
#
#
# class BelBankViewSet(GenericAPIView):
#     queryset = bankcurrency.models.BelBank.objects.all()
#     permissions_classes = (
#         permissions.IsAuthenticated
#     )
#     serializer_class = BelBankSerializer
#
#     def get(self, request):
#         if request.user.is_authenticated:
#             curr_req = requests.get(
#                 'https://belarusbank.by/api/kursExchange?city=Минск')
#             data = curr_req.json()
#             cur_rur_buy = data[0]['RUB_in']
#             cur_rur_sell = data[0]['RUB_out']
#             cur_eur_buy = data[0]['EUR_in']
#             cur_eur_sell = data[0]['EUR_out']
#             cur_usd_buy = data[0]['USD_in']
#             cur_usd_sell = data[0]['USD_out']
#
#             date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")
#
#             cur_new = BelBank.objects.create(eur_buy=cur_eur_buy, eur_sell=cur_eur_sell,
#                                              usd_buy=cur_usd_buy, usd_sell=cur_usd_sell, rur_buy=cur_rur_buy,
#                                              rur_sell=cur_rur_sell)
#             cur_new.save()
#             response = Response({'usd_buy': cur_usd_buy,
#                                  'usd_sell': cur_usd_sell,
#                                  'eur_buy': cur_eur_buy,
#                                  'eur_sell': cur_eur_sell,
#                                  'rur_buy': cur_rur_buy,
#                                  'rur_sell': cur_rur_sell,
#                                  'date': date_time_obj
#                                  })
#             return response
#         else:
#             return redirect('/unauchBB')
#
#     def specific_date(self):
#         """за определенную дату"""
#         cur_m = BelBank.objects.filter(date='2021.08.06')
#         return cur_m
#
#     def current_moment(self):
#         """за текущий момент"""
#         cur_mom = BelBank.objects.filter(date=datetime.now().strftime("%d-%m-%Y %H:%M"))
#         return cur_mom
#
#     def time_interval(self):
#         """за определенный промежуток времени"""
#         cur_mo = BelBank.objects.exclude(date=datetime.now()).filter(date=datetime.date(2021, 8, 4))
#         return cur_mo
#
#
# """Для неавторизированных пользователей"""
#
#
# class BelBankUnAuthViewSet(GenericAPIView):
#     queryset = bankcurrency.models.BelBank.objects.all()  # это наши объекты в базе данных
#     permissions_classes = (
#         permissions.AllowAny
#     )
#     serializer_class = BelBankUnAuthSerializer
#
#     def get(self, request):
#         curr_req = requests.get(
#             'https://belarusbank.by/api/kursExchange?city=Минск')
#         data = curr_req.json()
#         cur_rur_buy = data[0]['RUB_in']
#         cur_rur_sell = data[0]['RUB_out']
#         cur_eur_buy = data[0]['EUR_in']
#         cur_eur_sell = data[0]['EUR_out']
#         cur_usd_buy = data[0]['USD_in']
#         cur_usd_sell = data[0]['USD_out']
#         date_time_obj = datetime.now().strftime("%d-%m-%Y %H:%M")
#
#         response = Response({'usd_buy': cur_usd_buy,
#                              'usd_sell': cur_usd_sell,
#                              'eur_buy': cur_eur_buy,
#                              'eur_sell': cur_eur_sell,
#                              'rur_buy': cur_rur_buy,
#                              'rur_sell': cur_rur_sell,
#                              'date': date_time_obj
#                              })
#
#         return response
#
#     def post(self, *args):
#         pass
#
