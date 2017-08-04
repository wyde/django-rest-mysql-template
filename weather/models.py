# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class RainfallStation(models.Model):
    spk = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    sid = models.CharField(max_length=5)
    county = models.CharField(max_length=3)
    lon = models.FloatField()
    lat = models.FloatField()

    class Meta:
        verbose_name = "RainfallStation"
        verbose_name_plural = "RainfallStations"

    def __str__(self):
        return "%s %s %s" % (self.county, self.sid, self.name)

class Rainfall(models.Model):
    rpk = models.AutoField(primary_key=True)
    timestamp = models.CharField(max_length=25)
    r_10m = models.FloatField(blank=True, null=True)
    r_1h = models.FloatField(blank=True, null=True)
    r_3h = models.FloatField(blank=True, null=True)
    r_6h = models.FloatField(blank=True, null=True)
    r_12h = models.FloatField(blank=True, null=True)
    r_24h = models.FloatField(blank=True, null=True)
    r_td = models.FloatField(blank=True, null=True)
    r_yd = models.FloatField(blank=True, null=True)
    r_2d = models.FloatField(blank=True, null=True)
    station = models.ForeignKey(RainfallStation)

    class Meta:
        verbose_name = "Rainfall"
        verbose_name_plural = "Rainfalls"

    def __str__(self):
        return "%s %s %s" % (self.sid, self.name, self.timestamp)

