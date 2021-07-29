from rest_framework import serializers
from .models import AlfaBank, AlfaBankUnAuth, Company, Date


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AlfaBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlfaBank
        fields = '__all__'


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'


class AlfaBankUnAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlfaBankUnAuth
        fields = '__all__'
