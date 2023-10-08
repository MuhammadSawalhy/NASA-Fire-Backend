from django.db import models

class Sensor(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

class Reading(models.Model):
    co2 = models.DecimalField(max_digits=5, decimal_places=2)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reading for Sensor at {self.sensor.location} - CO2: {self.co2}"
