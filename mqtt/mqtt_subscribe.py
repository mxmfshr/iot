import sys
import os
from time import sleep
from Adafruit_IO import MQTTClient
import led

ADAFRUIT_IO_KEY = os.environ['IO_KEY']
ADAFRUIT_IO_USERNAME = os.environ['IO_USERNAME']

FEED_ID = 'test'

def connected(client):
    print('Listening for {0} changes...'.format(FEED_ID))
    client.subscribe(FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    print('Subscribed to {0}'.format(FEED_ID))

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

    # On
    if payload == '1':
        led.control('green', 'on')
    # Off
    elif payload == '0':
        led.control('green', 'off')

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

client.connect()

client.loop_blocking()

