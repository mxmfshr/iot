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

import sqlite3
import pandas as pd
from datetime import datetime

import curses


class MyService(myproto_pb2_grpc.MyServiceServicer):
    def __init__(self):
        self.conn = sqlite3.connect('./db.sqlite', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_table(self):
        return pd.DataFrame(self.cursor.execute("SELECT * FROM USERS"), columns=['id','card_id','card_text','last_used','status'])[['card_id', 'last_used', 'status']]

    def is_authorized(self, card_id):
        return True if (self.cursor.execute(f'SELECT COUNT(*) FROM authorized_users WHERE card_id = "{card_id}"').fetchall()[0][0]) > 0 else False

    def use_card(self, card_id):
        if not self.is_authorized(card_id):
            return "Not authorized"

        timestamp = datetime.now().strftime("%H:%M, %d %B %Y, %A")
        status = 'in' if (self.cursor.execute(f'SELECT status FROM users WHERE card_id = "{card_id}"').fetchall()[0][0]) == 'out' else 'out'
        update_query = f"""
        UPDATE
          users
        SET
          last_used = "{timestamp}",
          status = "{status}"
        WHERE card_id = {card_id}
        """
        self.cursor.execute(update_query)
        return "Card information updated"

    def SendData(self, request, context):
        id = request.id
        text = request.text
        res = self.use_card(id)
        #print(self.get_table())
        self.log()
        return myproto_pb2.Result(result=res)

    def log(self):
        curses.noecho()
        curses.cbreak()
        stdscr.addstr(0, 0, '{0}'.format(self.get_table()))
        stdscr.refresh()
        curses.noecho()
        curses.cbreak()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    myproto_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    stdscr = curses.initscr()
    serve()
    curses.endwin()

