from django.urls import path
from .views import AuthViewSet, UnAuthViewSet, FilterDateView, FilterDateIntervalView, FilterDateTodayView

urlpatterns = [
    path('rates/<bank>/', AuthViewSet.as_view()),
    path('sellrates/<bank>/', UnAuthViewSet.as_view()),
    path('date/', FilterDateView.as_view()),
    path('dateinterval/', FilterDateIntervalView.as_view()),
    path('datetoday/<banks>/', FilterDateTodayView.as_view()),
]
