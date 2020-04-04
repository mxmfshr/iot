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

import grpc

import myproto_pb2
import myproto_pb2_grpc

def get_sqrt(stub, val):
    req = myproto_pb2.Float(val=val)
    response = stub.GetSqrt(req)
    print(response.val)

def get_sigma(stub, val):
    reqs = [myproto_pb2.Float(val=v) for v in val]
    response = stub.GetSigma(iter(reqs))
    print(response.val)

def get_factors(stub, val):
    req = myproto_pb2.Float(val=val)
    responses = stub.GetFactors(req)
    for res in responses:
        print(res.val)

def get_max(stub, val):
    reqs = [myproto_pb2.Float(val=v) for v in val]
    responses = stub.GetMax(iter(reqs))    
    for res in responses:
        print(res.val)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = myproto_pb2_grpc.MyServiceStub(channel)
    print('sqrt of 4:')
    get_sqrt(stub, 4)
    print()

    print('std of [10,20,30,40,50]:')
    get_sigma(stub, [10,20,30,40,50])
    print()

    print('factors of 93:')
    get_factors(stub, 93)
    print()

    print('max of [3,4,1,6,2,3,7,10]:')
    get_max(stub, [3,4,1,6,2,3,7,10])    
    print()
    channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    run()
