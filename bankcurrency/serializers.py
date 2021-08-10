from rest_framework import serializers
from .models import AlfaBank, AlfaBankUnAuth, Company, BelApb, BelApbUnAuth, BelBank, BelBankUnAuth


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


class BelBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BelBank
        fields = '__all__'


class BelBankUnAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = BelBankUnAuth
        fields = '__all__'
