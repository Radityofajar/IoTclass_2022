import paho.mqtt.client as mqtt
import time
import json
import mysql.connector
import datetime

#MQTT
#mqttBroker ="mqtt.eclipseprojects.io"
mqttBroker ="210.123.42.157" 
Topic = "IoT_Class"
#username = 'if there is any'
#password = 'if there is any'

#Database
db_host = '113.198.211.95'
db_name = '5G_one'
table_name = 'IoTclass'

def on_message(client, userdata, message):
    raw_data = str(message.payload.decode("utf-8"))
    dht = json.loads(raw_data.replace("'",'"'))
    Temp = dht['temperature']
    Hum = dht['humidity']

    Time = datetime.datetime.now()
    try:
        mydb = mysql.connector.connect(
        host = f'{db_host}',
        user = 'admina',
        password = 'admina',
        database = f'{db_name}')

        mycursor = mydb.cursor()
        query = f"INSERT INTO {table_name} (Time, Temperature, Humidity) VALUES ('{Time}','{Temp}','{Hum}')"
        print('Query',query)
        mycursor.execute(query)
        mydb.commit()
        print('Commit success')

    except Exception as e:
        print(e)

    finally:
        mydb.close()
        time.sleep(3)


while True:
    client = mqtt.Client("My_Computer")
    #client.username_pw_set(f"{username}", f"{password}")
    client.connect(mqttBroker) 
    client.loop_start()
    client.subscribe(Topic)
    client.on_message=on_message 

    time.sleep(30)
    client.loop_stop()
