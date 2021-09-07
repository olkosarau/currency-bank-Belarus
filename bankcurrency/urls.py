from django.urls import path
from .views import AuthViewSet, UnAuthViewSet, FilterDateView, FilterDateIntervalView

urlpatterns = [
    path('currency/<bank>/', AuthViewSet.currency_bank_today),
    path('currencyUn/<bank>/', UnAuthViewSet.currency_bank_today),
    path('date/', FilterDateView.as_view()),
    path('dateinterval/', FilterDateIntervalView.as_view()),

]
