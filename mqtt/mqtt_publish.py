import sys
import os
import time
import RPi.GPIO as GPIO
from Adafruit_IO import MQTTClient
from mfrc522 import SimpleMFRC522

def rfid_message():
    reader = SimpleMFRC522()

    while True:
        try:
            id, text = reader.read()
            print(id)

        finally:
            time.sleep(1)
            GPIO.cleanup()
            return id

ADAFRUIT_IO_KEY = os.environ['IO_KEY']
ADAFRUIT_IO_USERNAME = os.environ['IO_USERNAME']

FEED_ID = 'test'

def connected(client):
    pass

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def publish(client, userdata, mid):
    print('data published')

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected

client.connect()

client.loop_background()

while True:
    text = rfid_message()
    client.publish(f'{FEED_ID}', text)
