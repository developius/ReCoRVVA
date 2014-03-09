#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#						main.py							  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)								  |
#	Thanks for contribution to B. James (benji@fxapi.co.uk) and A. Ledesma (monkeeyman@hotmail.co.uk) |
#---------------------------------------------------------------------------------------------------------+

# Import the various modules
from termcolor import colored
import socket, threading, os, time, math
import RPi.GPIO as GPIO
import os
import ping, motors, comms

# Setup the GPIOs
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

#Setup the Pan/Tilt Servos
servoNeutral = 7.5
servoRight = 12.5
servoLeft = 2.5
pan = GPIO.PWM(24,50)
tilt = GPIO.PWM(26,50)
pan.start(7.5)
tilt.start(7.5)

print colored("Robot ping and control script, written in Python", 'magenta')
print colored("Let\'s drive!", 'magenta')
print(" ")

#Start the camera feed
os.system('./startstream.sh &> /dev/null')

print colored("Leaving time for camera warmup, please wait", 'red')
time.sleep(2)

#Start Ping thread and Communication threads
print colored("Waiting for client connection...", 'yellow')
comms.Comms().start()
ping.Ping().start()
