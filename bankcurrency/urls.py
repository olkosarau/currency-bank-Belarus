from django.urls import path
from .views import AuthViewSet, UnAuthViewSet, FilterDateView, FilterDateIntervalView

urlpatterns = [
    path('rates/<bank>/', AuthViewSet.currency_bank_today),
    path('sellrates/<bank>/', UnAuthViewSet.currency_bank_now),
    path('date/', FilterDateView.as_view()),
    path('dateinterval/', FilterDateIntervalView.as_view()),

]
