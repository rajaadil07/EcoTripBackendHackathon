from rest_framework import serializers
from .models import CarbonFootprint

class CarbonFootprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonFootprint
        fields = '__all__'