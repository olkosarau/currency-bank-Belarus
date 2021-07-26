# from django.contrib.sites import requests
# from rest_framework.generics import GenericAPIView
# from rest_framework import viewsets, permissions
# import bankcurrency
# from .serializers import AlfaBankSerializer
# import APIResponse
#
# class AlfaBankViewSet(viewsets.GenericAPIView):
#     queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
#     permissions_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = AlfaBankSerializer
#
#
#
#
# # #class MyCronJob(CronJobBase):
# #     RUN_AT_TIMES = ['03:00'] # the currency rates update time
# #     def __init__(self):
# #         self.r = requests.get(URL)
# #
# #     schedule = Schedule(run_at_times=RUN_AT_TIMES)
# #     code = 'cron.MyCronJob'
# #
# #     def do(self):
# #         response = self.r.json()
# #         currency = response['rates']
# #         usd = currency['USD']
# #         rur = currency['RUR']
# #         eur = currency['EUR']
# #         now = datetime.datetime.now()
# #         RatesData.objects.filter(id='1').update(usd=usd, rur=rur, eur=eur, date=now)