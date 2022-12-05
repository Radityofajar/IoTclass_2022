#import all the libraries
import paho.mqtt.client as mqtt
import time
import serial
import json

arduino_nano = serial.Serial('COM4', 9600, timeout=.1)

def on_message(client, userdata, message):
    raw_data = str(message.payload.decode("utf-8"))
    print(raw_data)
    dht = json.loads(raw_data.replace("'",'"'))
    Temp = dht['temperature']
    Hum = dht['humidity']

    if Temp > 30 or Hum > 40:
        thresh = '1'
    elif (Temp > 25 and Temp < 30) or (Hum > 15 and Hum < 40) :
        thresh = '2'
    elif (Temp == 25) or (Hum == 30) :
        thresh = '3'
    else:
        thresh = '4'
        
    arduino_nano.write(thresh.encode())
#mqttBroker ="mqtt.eclipseprojects.io"
mqttBroker ="210.123.42.157" 
Topic = "IoT_Class"

client = mqtt.Client("User_device")
#client.username_pw_set("Unknown", "Unknown")

client.connect(mqttBroker) 
client.subscribe(Topic)
client.on_message=on_message 
client.loop_forever()
