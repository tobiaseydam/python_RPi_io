from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import gpioPin
import rpyc

class gpioPinListView(ListView):
    model = gpioPin
    template_name = "gpio_manager/index.html"
    context_object_name = "gpio"
    extra_context = {
                "title" : "Raspberry Pi GPIOs",
                #"rows" : [(gpioPin.objects.all()[left], gpioPin.objects.all()[right]) for (left, right) in list(zip(range(0,41,2), range(1,41,2)))],
                "rows" : [(left, right) for (left, right) in list(zip(range(0,41,2), range(1,41,2)))],
            }
    

class gpioPinDetailView(DetailView):
    model = gpioPin
    extra_context = {
                "title" : "Raspberry Pi GPIO"
                }

class gpioPinUpdateView(UpdateView):
    model = gpioPin
    fields = ["connected", "device", "mqtt_alias", "gpio"]
    extra_context = {
                "title" : "Raspberry Pi GPIO Bearbeiten"
                }
    
    def form_valid(self, form):
        try:
            conn = rpyc.connect("localhost", 18830)
            c = conn.root
            if form.instance.connected:
                print("Add/Update Pin {}".format(form.instance.gpio))
                c.add_dht22(form.instance.gpio, form.instance.mqtt_alias)
            else:
                print("Remove Pin {}".format(form.instance.gpio))
                c.remove_dht22(form.instance.gpio)
            
        except Exception as e:
            print(e)
            
        return super().form_valid(form)






























