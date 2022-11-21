import paho.mqtt.client as mqtt
import time
import json
import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host ='113.198.211.95',
    user = 'admina',
    password = 'admina',
    database = '5G_one')
table_name = 'IoTclass'
def on_message(client, userdata, message):
    raw_data = str(message.payload.decode("utf-8"))
    print("received message: " ,str(message.payload.decode("utf-8")))
    dht = json.loads(raw_data.replace("'",'"'))
    print('DHT json: ',dht)

    Temp = dht['temperature']
    print('Temperature: ',Temp)
    Hum = dht['humidity']
    print('Humidity: ', Hum)

    Time = datetime.datetime.now()
    try:
        mycursor = mydb.cursor()
        query = f"INSERT INTO {table_name} (Time, Temperature, Humidity) VALUES ('{Time}','{Temp}','{Hum}')"
        print('Query',query)
        mycursor.execute(query)
        mydb.commit()
        print('Commit success')
    except Exception as e:
        print(e)
    finally:
        time.sleep(3)

#mqttBroker ="mqtt.eclipseprojects.io"
mqttBroker ="210.123.42.157" 
Topic = "IoT_Class"

client = mqtt.Client("My_Computer")
#client.username_pw_set("username", "password")
client.connect(mqttBroker) 
client.loop_start()
client.subscribe(Topic)
client.on_message=on_message 

time.sleep(30)
client.loop_stop()