from django.db import models

# Create your models here.
class Truck(models.Model):
    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('truck name', max_length=100)
    latitude = models.FloatField('latitude')
    longitude = models.FloatField('longitude')
    address = models.CharField('address', max_length=100)
    food_items = models.CharField('food_items', max_length=256)
