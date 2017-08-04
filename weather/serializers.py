from rest_framework import serializers
from weather.models import Rainfall, RainfallStation

class RainfallStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainfallStation
        fields = '__all__' 

class RainfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rainfall
        fields = '__all__' 

