import serial
import json
from IoTown_api import data
import time
import datetime
import mysql.connector

url = "https://town.coxlab.kr"
token = "089d5279cdb90b2b41b0cc4b96be8be9450e44bbbfc3c3dcfb534d217353af7a"
nodeid = "LW111100001111AFFF"

mydb = mysql.connector.connect(
    host ='113.198.211.95',
    user = 'admina',
    password = 'admina',
    database = '5G_one'
)

ser = serial.Serial('COM3', 115200)

while True:
    raw_data = (ser.readline().decode('utf-8').rstrip())
    #print('rawdata: ', raw_data)
    dht = json.loads(raw_data.replace("'",'"'))
    print('DHT json: ',dht)
    #print(type(dht))

    r = data(url,token,nodeid,dht)

    Time = datetime.datetime.now()
    Temperature = dht['temperature']
    Humidity = dht['humidity']
    try:
        mycursor = mydb.cursor()
        query = f"INSERT INTO IoTclass (Time, Temperature, Humidity) VALUES ('{Time}','{Temperature}','{Humidity}')"
        #print(query)
        mycursor.execute(query)
        mydb.commit()
        print('Commit success')
    except Exception as e:
        print(e)
    finally:
        time.sleep(3)