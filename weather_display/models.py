from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=128)
    has_rain = models.BooleanField(default=False)
    has_temp = models.BooleanField(default=False)
    has_humidity = models.BooleanField(default=False)
    has_wind_speed = models.BooleanField(default=False)
    has_wind_dir = models.BooleanField(default=False)
    has_lux = models.BooleanField(default=False)
    has_pressure = models.BooleanField(default=False)


class Reading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    rain = models.DecimalField(max_digits=5, decimal_places=3)
    temp = models.DecimalField(max_digits=6, decimal_places=3)
    humidity = models.DecimalField(max_digits=5, decimal_places=3)
    wind_speed = models.DecimalField(max_digits=6, decimal_places=3)
    wind_dir = models.DecimalField(max_digits=6, decimal_places=3)
    lux = models.DecimalField(max_digits=6, decimal_places=3)
    pressure = models.DecimalField(max_digits=7, decimal_places=3)
