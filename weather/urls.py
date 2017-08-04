from django.conf.urls import url, include
from rest_framework import routers
from weather.views import RainfallViewSet, RainfallStationViewSet


router = routers.DefaultRouter()
router.register(r'rainfalls', RainfallViewSet)
router.register(r'stations', RainfallStationViewSet)

urlpatterns = router.urls

