#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import socket # client

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',6999))
while True:
    msg = 'Hello world!'
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('recv:',data.decode())
    time.sleep(1)
client.close()
