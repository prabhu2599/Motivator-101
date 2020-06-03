from rest_framework import serializers
from .models import AstroModel


class AstroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstroModel
        fields = '__all__'
