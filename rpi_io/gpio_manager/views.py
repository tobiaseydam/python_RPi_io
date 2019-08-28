from django.shortcuts import render
from django.views.generic import ListView
from .models import gpioPin

gpio = [
            {
            "row": 0,
            "left": {
                    "id":1,
                    "func1": "3V3",
                    "func2": "Power",
                    "color": "red"
                    },
            "right": {
                    "id":2,
                    "func1": "5V",
                    "func2": "Power",
                    "color": "red"
                    }
            },{
            "row": 1,
            "left": {
                    "id":3,
                    "func1": "GPIO2",
                    "func2": "SDA1 I2C",
                    "color": "yellow",
                    "conn" : True
                    },
            "right": {
                    "id":4,
                    "func1": "5V",
                    "func2": "Power",
                    "color": "red"
                    }
            },{
            "row": 2,
            "left": {
                    "id":5,
                    "func1": "GPIO13",
                    "func2": "SCL1 I2C",
                    "color": "yellow",
                    "conn" : True
                    },
            "right": {
                    "id":6,
                    "func1": "Ground",
                    "color": "grey"
                    }
            },{
            "row": 3,
            "left": {
                    "id":7,
                    "func1": "GPIO4",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":8,
                    "func1": "GPIO14",
                    "func2": "UART0_TXD",
                    "color": "blue",
                    "conn" : True
                    }
            },{
            "row": 4,
            "left": {
                    "id":9,
                    "func1": "Ground",
                    "color": "grey"
                    },
            "right": {
                    "id":10,
                    "func1": "GPIO15",
                    "func2": "UART0_RXD",
                    "color": "blue",
                    "conn" : True
                    }
            },{
            "row": 5,
            "left": {
                    "id":11,
                    "func1": "GPIO17",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":12,
                    "func1": "GPIO18",
                    "func2": "PCM_CLK",
                    "color": "green",
                    "conn" : True
                    }
            },{
            "row": 6,
            "left": {
                    "id":13,
                    "func1": "GPIO27",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":14,
                    "func1": "Ground",
                    "color": "grey"
                    }
            },{
            "row": 7,
            "left": {
                    "id":15,
                    "func1": "GPIO22",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":16,
                    "func1": "Ground",
                    "color": "green"
                    }
            },{
            "row": 8,
            "left": {
                    "id":17,
                    "func1": "3V3",
                    "func2": "Power",
                    "color": "red"
                    },
            "right": {
                    "id":18,
                    "func1": "GPIO24",
                    "color": "green",
                    "conn" : True
                    }
            },{
            "row": 9,
            "left": {
                    "id":19,
                    "func1": "GPIO10",
                    "func2": "SPI0_MOSI",
                    "color": "blue",
                    "conn" : True
                    },
            "right": {
                    "id":20,
                    "func1": "Ground",
                    "color": "grey"
                    }
            },{
            "row": 10,
            "left": {
                    "id":21,
                    "func1": "GPIO09",
                    "func2": "SPI0_MISO",
                    "color": "blue",
                    "conn" : True
                    },
            "right": {
                    "id":22,
                    "func1": "GPIO25",
                    "color": "green",
                    "conn" : True
                    }
            },{
            "row": 11,
            "left": {
                    "id":23,
                    "func1": "GPIO11",
                    "func2": "SPI0_SCLK",
                    "color": "blue",
                    "conn" : True
                    },
            "right": {
                    "id":24,
                    "func1": "GPIO08",
                    "func2": "SPI0_CE0_EN",
                    "color": "blue",
                    "conn" : True
                    }
            },{
            "row": 12,
            "left": {
                    "id":25,
                    "func1": "Ground",
                    "color": "grey"
                    },
            "right": {
                    "id":26,
                    "func1": "GPIO07",
                    "func2": "SPI0_CE1_EN",
                    "color": "blue",
                    "conn" : True
                    }
            },{
            "row": 13,
            "left": {
                    "id":27,
                    "func1": "ID_SD",
                    "func2": "I2C ID EEPROM",
                    "color": "yellow"
                    },
            "right": {
                    "id":28,
                    "func1": "ID_SC",
                    "func2": "I2C ID EEPROM",
                    "color": "yellow"
                    }
            },{
            "row": 14,
            "left": {
                    "id":29,
                    "func1": "GPIO05",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":30,
                    "func1": "Ground",
                    "color": "grey"
                    }
            },{
            "row": 15,
            "left": {
                    "id":31,
                    "func1": "GPIO06",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":32,
                    "func1": "GPIO12",
                    "color": "green",
                    "conn" : True
                    }
            },{
            "row": 16,
            "left": {
                    "id":33,
                    "func1": "GPIO13",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":34,
                    "func1": "Ground",
                    "color": "grey"
                    }
            },{
            "row": 17,
            "left": {
                    "id":35,
                    "func1": "GPIO19",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":36,
                    "func1": "GPIO16",
                    "color": "green",
                    "conn" : True
                    }
            },{
            "row": 18,
            "left": {
                    "id":37,
                    "func1": "GPIO26",
                    "color": "green",
                    "conn" : True
                    },
            "right": {
                    "id":38,
                    "func1": "GPIO20",
                    "color": "green",
                    "conn" : True
                    }
            },{
            "row": 19,
            "left": {
                    "id":39,
                    "func1": "Ground",
                    "color": "grey"
                    },
            "right": {
                    "id":40,
                    "func1": "GPIO21",
                    "color": "green",
                    "conn" : True
                    }
            }
        
        ]

def home(request):
    
    
    context = {
                "title" : "Raspberry Pi GPIOs",
                "gpio"  : gpio
            }
    
    
    return render(request, "gpio_manager/index.html", context)

class gpioPinListView(ListView):
    model = gpioPin
    template_name = "gpio_manager/index.html"
    context_object_name = "gpio"
    extra_context = {
                "title" : "Raspberry Pi GPIOs",
                "rows" : [(gpioPin.objects.all()[left], gpioPin.objects.all()[right]) for (left, right) in list(zip(range(0,41,2), range(1,41,2)))]
            }




































