#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#						main.py							  |
# Hamdles the multithreading and the other scripts.                                                       |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk) and B. James (musicboyben1999@gmail.com)	                  |
#---------------------------------------------------------------------------------------------------------+

# Import the various modules
from termcolor import colored
import socket, threading, os, time, math
import RPi.GPIO as GPIO
import sensors, motors, comms, cam

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

def start():
	print colored("Robot ping and control script, written in Python", 'magenta')
	print colored("Let's go!\n", 'magenta')

	#Start the camera feed
	cam.camera("CamOn")

	print colored("Leaving time for camera warmup, please wait", 'red')
	time.sleep(1)

	#Start Sensors and Communication threads
	comms.Comms().start()
	sensors.Ping().start()
	sensors.Temp().start()
