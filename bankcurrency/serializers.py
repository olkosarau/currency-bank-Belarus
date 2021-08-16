from rest_framework import serializers
from .models import Auth, UnAuth


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = '__all__'


class UnAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnAuth
        fields = '__all__'

