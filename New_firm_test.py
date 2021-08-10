#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#MAME DRONE

#2018_국제문화재산업전_Tello_시연_스크립트 0.0.1 alpha

#For Tello Firmware v_01.04.35.01

#by.김성욱 AKA pangin @개발팀 in MAME DRONE as CTO

#in memory #수리_들어간다!

"""
from Library import tello
import threading
import socket
import sys
import time

Tello_IP = "192.168.10.2"
Tello_port = 8888
Tello = tello.Tello(Tello_IP, Tello_port)
Tello.takeoff()
time.sleep(5)
Tello.set_speed(1)
time.sleep(1)
Tello.move_forward(1)
time.sleep(5)
Tello.rotate_cw(180)
time.sleep(5)
Tello.move_forward(1)
time.sleep(5)
Tello.land()
print("Flight time: %s" % Tello.get_flight_time())
"""

import threading
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

def tello(command):
    try:
        msg = command

        if not msg:
            print("[WARN] Noting to tell\n")

        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        exit()

print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

"""
while True: 

    try:
        msg = input("");

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break
"""

