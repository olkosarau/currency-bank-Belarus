from django.urls import path
from .views import AuthViewSet, UnAuthViewSet, FilterDateView, FilterDateIntervalView, FilterDateTodayView

urlpatterns = [
    path('rates/<bank>/', AuthViewSet.currency_bank_now),
    path('sellrates/<bank>/', UnAuthViewSet.currency_bank_now),
    path('date/', FilterDateView.as_view()),
    path('dateinterval/', FilterDateIntervalView.as_view()),
    path('datetoday/<banks>/', FilterDateTodayView.currency_bank_today),
]
