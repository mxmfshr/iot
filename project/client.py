# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging
import time

import grpc

import myproto_pb2
import myproto_pb2_grpc

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def send_data(stub, id, text):
    req = myproto_pb2.Card(id=id, text=text)
    response = stub.SendData(req)
    print(response.result)


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = myproto_pb2_grpc.MyServiceStub(channel)
    reader = SimpleMFRC522()

    while True:
        id, text = reader.read()
        send_data(stub, id, text)
        time.sleep(1)
    
    GPIO.cleanup()
    channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    run()
