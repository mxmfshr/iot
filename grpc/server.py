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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import myproto_pb2
import myproto_pb2_grpc

import math
import numpy as np
from functools import reduce

class MyService(myproto_pb2_grpc.MyServiceServicer):
    def GetSqrt(self, request, context):
        return myproto_pb2.Float(val=math.sqrt(request.val))

    def GetSigma(self, request_iterator, context):
        return myproto_pb2.Float(val=np.std([v.val for v in request_iterator]))

    def GetFactors(self, request, context):
        for v in iter(set(reduce(list.__add__, ([i, request.val//i] for i in range(1, int(request.val**0.5) + 1) if request.val % i == 0)))):
            yield myproto_pb2.Float(val=v)

    def GetMax(self, request_iterator, context):
        cur_max = None
        for v in request_iterator:
            if not cur_max or v.val > cur_max:
                cur_max = v.val
                yield myproto_pb2.Float(val=cur_max)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myproto_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
