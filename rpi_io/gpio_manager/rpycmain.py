# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:44:43 2019

@author: Tobias
"""

from rpyc.utils.server import ThreadedServer
from threading import Thread
import time
import rpyc
import paho.mqtt.client as mqtt
import Adafruit_DHT
import json

last_message = None

interval = 10

def mqtt_onConnect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    
def mqtt_onMessage(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = mqtt_onConnect
mqtt_client.on_message = mqtt_onMessage

try:
    with open("config.json", "r") as f:
        sensorList = json.load(f)
except:
    sensorList = {}

class RypcMqttService(rpyc.Service):
    def exposed_send_message(self, topic, message):
        print("Sending message... {}".format(topic))
        mqtt_client.publish(topic, payload=message)
    
    def exposed_get_last_message(self):
        return last_message
    
    def exposed_stop_server(self):
        mqtt_client.disconnect()
        mqtt_client.loop_stop()
        server.close()
        
    def exposed_add_dht22(self, pin, topic):
        print("Add DHT22 on Pin {} with topic {}".format(pin, topic))
        sensorList[pin] = {"sensor": Adafruit_DHT.DHT22, "pin": pin, "topic": topic}
        self.save()
        
    def exposed_remove_dht22(self, pin):
        if pin in sensorList:
            del sensorList[pin]
        self.save()
    
    def save(self):
        with open("config.json", "w") as f:
            json.dump(sensorList, f)
            
    #def load(self):
    #    global sensorList
    #    with open("config.json", "r") as f:
    #        sensorList = json.load(f)
        

try:
    server = ThreadedServer(RypcMqttService, port=18830)

    t = Thread(target = server.start)
    t.daemon = True
    
    t.start()
    
    mqtt_client.connect("192.168.178.23", 1883, 60)
    mqtt_client.loop_start()
    
    i = 0
    while True:
        i+=1
        for s in list(sensorList.keys()):
                sens = sensorList[s]
                hum, temp = Adafruit_DHT.read_retry(sens["sensor"], sens["pin"], retries=2)
                if hum is not None and temp is not None:    
                    data = {"humidity": hum, "temperature": temp}
                    mqtt_client.publish(sens["topic"], json.dumps(data))
                    print("{} - Hum: {:.2f} % / Temp: {:.2f} °C".format(sens["topic"], hum, temp))
        time.sleep(interval)
        
except Exception as e:
    print("Error: {}".format(e))
    mqtt_client.disconnect()
    mqtt_client.loop_stop()
    server.close()

#i = 0
#while True:
#    i+=1
#    time.sleep(1)
