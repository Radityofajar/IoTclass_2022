import requests
import serial
import json
import time

ser = serial.Serial('COM3', 115200)

while True:
    raw_data = (ser.readline().decode('utf-8').rstrip())
    dht = json.loads(raw_data.replace("'",'"'))
    print('DHT json: ',dht)
    Temp = dht['temperature']
    print(Temp)
    Hum = dht['humidity']
    print(Hum)
    response = requests.get(f"https://api.thingspeak.com/update?api_key=5ACTQH3SXOY22XMY&field1={Temp}&field2={Hum}")

    time.sleep(3)