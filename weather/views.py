from django.shortcuts import render

# Create your views here.
from weather.models import Rainfall, RainfallStation
from weather.serializers import RainfallSerializer, RainfallStationSerializer
from rest_framework import viewsets

class RainfallViewSet(viewsets.ModelViewSet):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer

class RainfallStationViewSet(viewsets.ModelViewSet):
    queryset = RainfallStation.objects.all()
    serializer_class = RainfallStationSerializer
    
