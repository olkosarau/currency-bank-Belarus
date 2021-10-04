from rest_framework import serializers
from .models import CurrencyAuthUser, CurrencyUnAuthUser


class CurrencyAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyAuthUser
        fields = '__all__'


class CurrencyUnAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyUnAuthUser
        fields = '__all__'
