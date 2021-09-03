from django.urls import path
from .views import AuthViewSet, UnAuthViewSet, FilterDateView, FilterDateIntervalView

urlpatterns = [

    path('alfabank', AuthViewSet.currency_alfa_bank_today),
    path('belagro', AuthViewSet.currency_bel_agro_today),
    path('belbank', AuthViewSet.currensy_belarus_bank_today),
    path('alfabankUn', UnAuthViewSet.currency_alfa_bank_today),
    path('belagroUn', UnAuthViewSet.currency_bel_agro_today),
    path('belbankUn', UnAuthViewSet.currensy_belarus_bank_today),
    path('datetoday/', FilterDateView.as_view()),
    path('dateinterval/', FilterDateIntervalView.as_view()),



]