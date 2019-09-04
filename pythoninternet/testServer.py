#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6999)) # bind listening port
server.listen(5) # listening

count=0
while True:# 
    # conn is a instence of c/s connection
    conn,addr = server.accept() # wait for connections, bad behavior when receiving multiple connection
    print(conn,addr)
    while True:
        try:
            data = conn.recv(1024).decode()
            if data=='':
                print('Error connection closed')
                break

            print('recive:',str(count).encode())
            conn.send(str(count).encode())
            count=count+1
        except ConnectionResetError as e:
            print('Error connection closed')
            break
    conn.close()