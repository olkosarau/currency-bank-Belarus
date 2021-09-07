from django.urls import path
from .views import AuthViewSet, UnAuthViewSet, FilterDateView, FilterDateIntervalView, FilterDateTodayView

urlpatterns = [
    path('currency/<bank>/', AuthViewSet.currency_bank_today),
    path('currency/<bank>/', UnAuthViewSet.currency_bank_today),
    path('date/', FilterDateView.as_view()),
    path('dateinterval/', FilterDateIntervalView.as_view()),
    path('datetoday/', FilterDateTodayView.as_view())
]
