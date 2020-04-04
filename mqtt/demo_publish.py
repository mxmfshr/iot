import sys
import os
from Adafruit_IO import MQTTClient

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
    text = input()
    client.publish(f'{FEED_ID}', text)
