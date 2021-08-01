from django.urls import path
from rest_framework import routers
from .views import AlfaBankViewSet, DateViewSet, AlfaBankUnAuthViewSet

urlpatterns = [
    #path('company/', CompanyViewSet.as_view()),
    path('', AlfaBankViewSet.as_view()),
    path('Date/', DateViewSet.as_view()),
    path('AlfaBankUnAuch/', AlfaBankUnAuthViewSet.as_view()),
]