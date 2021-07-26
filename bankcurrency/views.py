from django.shortcuts import render
from django.http import HttpResponse
import requests
from rest_framework import viewsets, permissions
from rest_framework.generics import GenericAPIView
import bankcurrency
from .models import AlfaBank
from .serializers import AlfaBankSerializer
from rest_framework.views import APIView, Response, Request
import APIResponse

class AlfaBankViewSet(GenericAPIView):
    queryset = bankcurrency.models.AlfaBank.objects.all()  # это наши объекты в базе данных
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AlfaBankSerializer

    def get(self, request, format=None):
        # if request.user.is_authenticated:   # Проверка на аторизацию
        curr_req = requests.get('GET/public/rates')  # Делаем запрос в АПИ

        response = APIResponse(curr_req)
        return response



    @classmethod
    def get_extra_actions(cls):
        return []