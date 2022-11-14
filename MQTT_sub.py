
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

#mqttBroker ="mqtt.eclipseprojects.io"
mqttBroker ="210.123.42.157" 
Topic = "TEMPERATURE"

client = mqtt.Client("User_device")
#client.username_pw_set("username", "password")
client.connect(mqttBroker) 

client.loop_start()
client.subscribe(Topic)
client.on_message=on_message 

time.sleep(30)
client.loop_stop()