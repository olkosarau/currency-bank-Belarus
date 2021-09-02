from django.urls import path
from .views import AuthViewSet, UnAuthViewSet

urlpatterns = [

    path('alfabank', AuthViewSet.currency_alfa_bank_today),
    path('belagro', AuthViewSet.currency_bel_agro_today),
    path('belbank', AuthViewSet.currensy_belarus_bank_today),
    path('alfabankUn', UnAuthViewSet.currency_alfa_bank_today),
    path('belagroUn', UnAuthViewSet.currency_bel_agro_today),
    path('belbankUn', UnAuthViewSet.currensy_belarus_bank_today),
    path('datecurrent', AuthViewSet.date_get_queryset),
    path('dateinterval', AuthViewSet.interval_get_queryset),


]