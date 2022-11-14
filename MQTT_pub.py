import paho.mqtt.client as mqtt 
from random import uniform
import time

#mqttBroker ="mqtt.eclipseprojects.io" 
mqttBroker ="210.123.42.157" 

client = mqtt.Client("Sensor_Temperature_1")
#client.username_pw_set("username", "password")
client.connect(mqttBroker)
Topic = "TEMPERATURE"

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish(Topic, randNumber)
    print("Just published " + str(randNumber) + f" to topic {Topic}")
    time.sleep(1)