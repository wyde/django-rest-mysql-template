from django.contrib import admin

# Register your models here.
from .models import Rainfall, RainfallStation

admin.site.register(Rainfall)
admin.site.register(RainfallStation)

