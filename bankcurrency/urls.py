from django.urls import path
from rest_framework import routers
from .views import AlfaBankViewSet

urlpatterns = [
    path('', AlfaBankViewSet.as_view()),
]