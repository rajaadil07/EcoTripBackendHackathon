from django.db import models

class CarbonFootprint(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.FloatField(default=0.0)
    car_gasoline = models.FloatField(default=0.0)
    car_diesel = models.FloatField(default=0.0)
    car_electric = models.FloatField(default=0.0)
    bus = models.FloatField(default=0.0)
    train = models.FloatField(default=0.0)
    airplane = models.FloatField(default=0.0)
    biking = models.FloatField(default=0.0)
    walking = models.FloatField(default=0.0)
    chat_gpt_response = models.TextField(null=True, blank=True)
