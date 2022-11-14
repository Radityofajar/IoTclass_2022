import paho.mqtt.client as mqtt 
from random import uniform
import time
import json
import serial

mqttBroker ="mqtt3.thingspeak.com" 

client = mqtt.Client("HAMJITk3LDQ8MCQtJwAyKRA")
client.username_pw_set("HAMJITk3LDQ8MCQtJwAyKRA", "Kf56p4KlSAFSnZyfCrJoyuCU")
client.ws_set_options("/mqtt")
client.connect(mqttBroker)
Topic = "channels/1934796/publish"

ser = serial.Serial('COM3', 115200)

while True:
    raw_data = (ser.readline().decode('utf-8').rstrip())
    dht = json.loads(raw_data.replace("'",'"'))
    print('DHT json: ',dht)
    Temp = dht['temperature']
    print(Temp)
    Hum = dht['humidity']
    print(Hum)
    payload = f"field1={Temp}&field2={Hum}"
    client.publish(Topic, payload)
    time.sleep(1)