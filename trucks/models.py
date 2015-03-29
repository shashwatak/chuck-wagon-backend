from django.db import models

# Create your models here.
class Truck(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    name = models.CharField('truck name', max_length=100)
