from rest_framework import serializers
from .models import AlfaBank, AlfaBankUnAuth, Company, BelApb, BelApbUnAuth


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AlfaBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlfaBank
        fields = '__all__'


class AlfaBankUnAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlfaBankUnAuth
        fields = '__all__'


class BelApbSerializer(serializers.ModelSerializer):
    class Meta:
        model = BelApb
        fields = '__all__'


class BelApbUnAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = BelApbUnAuth
        fields = '__all__'