from django.db import models
from django.urls import reverse
# Create your models here.

class gpioPin(models.Model):
    pin = models.IntegerField()
    row = models.IntegerField()
    func1 = models.CharField(max_length=32)
    func2 = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    connectable = models.BooleanField()
    connected = models.BooleanField()
    device = models.CharField(max_length=32, blank=True)
    mqtt_alias = models.CharField(max_length=32, blank=True)
    gpio = models.IntegerField()
    
    
    def get_absolute_url(self):
        return reverse("gpio_manager-overview")