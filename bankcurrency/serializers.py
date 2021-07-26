from rest_framework import serializers
from .models import AlfaBank


class AlfaBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlfaBank
        fields = '__all__'

