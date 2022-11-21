import paho.mqtt.client as mqtt 
import time
import serial

#mqttBroker ="mqtt.eclipseprojects.io" 
mqttBroker ="210.123.42.157" 

client = mqtt.Client("Sensor_Temperature_1")
#client.username_pw_set("username", "password")
client.connect(mqttBroker)
Topic = "IoT_Class"
ser = serial.Serial('COM3', 115200)

while True:
    payload = (ser.readline().decode('utf-8').rstrip())
    client.publish(Topic, payload)
    print("Just published " + str(payload) + f" to topic {Topic}")
    time.sleep(1)