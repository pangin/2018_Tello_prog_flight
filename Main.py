# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# MAME DRONE

# 2018_국제문화재산업전_Tello_시연_스크립트 0.0.1 alpha

# For Tello Firmware v_01.04.35.01

# by.김성욱 AKA pangin @개발팀 in MAME DRONE as CTO

# In memory
#수리_들어간다!


from Library import tello
import time
# import logging

# Variable for Tello
Tello_IP = "192.168.10.3"
Tello_port = 8888
Tello = tello.Tello(Tello_IP, Tello_port, imperial = False)

# Variable for logger
"""
logger = logging.getLoger("Tello_control_logger")
logger.setLevel(logging.DEBUG)
"""

# User Function
def get_before_battery():
    before_battery = Tello.get_battery()
    print("[INFO] Battery Level: %s\n" % before_battery)
    return before_battery

def read_avr_battery():
    battery_data = open('bat.txt', 'r')
    avr_battery = battery_data.readline()
    battery_data.close()
    print("[INFO] Average Battery Usage: %s\n" % avr_battery)
    return avr_battery

def write_avr_battery(avr_battery):
    battery_data = open('bat.txt', "w")
    battery_data.write(avr_battery)
    battery_data.close()
    print("[INFO] ")

def calc_avr_battery(before_battery, after_battery):
    avr_battery = before_battery - after_battery
    return avr_battery


# Custom Variable
left = "left"
right = "right"
up = "up"
down = "down"
forward = "forward"
back = "back"
loop = True
avr_battery_level = ""

# Make It Rain!
"""
while loop is True:
    before_flight_battery = get_before_battery()
    avr_battery_level = read_avr_battery()
    if avr_battery_level > before_flight_battery:
        print("[WARN] Battery level is too low to start mission! Can't take off. Please recharge or change battery.\n")
        loop = False
    elif avr_battery_level < before_flight_battery:
        print("[INFO] Take off.\n")
        Tello.takeoff()
        time.sleep(5)
        print("[INFO] Set speed to 100\n")
        Tello.set_speed(100)
        time.sleep(5)
        Tello.move_right(20)
        time.sleep(5)
        Tello.rotate_ccw(90)
        time.sleep(5)
        Tello.move_right(20)
        time.sleep(5)
        Tello.rotate_ccw(90)
        time.sleep(5)
        Tello.move_right(20)
        time.sleep(5)
        Tello.rotate_ccw(90)
        time.sleep(5)
        Tello.move_right(20)
        time.sleep(5)
        Tello.rotate_ccw(90)
        time.sleep(5)
        Tello.land()
        print("[INFO] Flight time: %s\n" % Tello.get_flight_time())
        time.sleep(5)
        after_flight_battery = Tello.get_battery()
        print("[INFO] Battery Level: %s\n" % after_flight_battery)
        used_battery = calc_avr_battery(before_flight_battery, after_flight_battery)
        write_avr_battery(used_battery)
    else:
        print("[ERROR] Unknown error!")
        loop = False
print("[INFO] Program Terminated.")
"""
Tello.takeoff()
time.sleep(2)
Tello.move_down(30)
time.sleep(2)
print("[INFO] Set speed to 100\n")
Tello.set_speed(100)
time.sleep(2)
Tello.move_right(50)
time.sleep(2)
Tello.rotate_ccw(90)
time.sleep(2)
Tello.move_right(50)
time.sleep(2)
Tello.rotate_ccw(90)
time.sleep(2)
Tello.move_right(50)
time.sleep(2)
Tello.rotate_ccw(90)
time.sleep(2)
Tello.move_right(50)
time.sleep(2)
Tello.rotate_ccw(90)
time.sleep(2)
Tello.land()
print("[INFO] Flight time: %s\n" % Tello.get_flight_time())
time.sleep(5)
after_flight_battery = Tello.get_battery()
print("[INFO] Battery Level: %s\n" % after_flight_battery)
print("[INFO] Program Terminated.")