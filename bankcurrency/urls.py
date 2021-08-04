from django.urls import path
from rest_framework import routers
from .views import AlfaBankViewSet, DateViewSet, AlfaBankUnAuthViewSet

urlpatterns = [
    #path('company/', CompanyViewSet.as_view()),
    path('bank', AlfaBankViewSet.as_view(), name='bank'),
    path('now', AlfaBankUnAuthViewSet.as_view()),
]