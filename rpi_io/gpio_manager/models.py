from django.db import models

# Create your models here.

class gpioPin(models.Model):
    pin = models.IntegerField()
    row = models.IntegerField()
    func1 = models.CharField(max_length=32)
    func2 = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    connectable = models.BooleanField()
    