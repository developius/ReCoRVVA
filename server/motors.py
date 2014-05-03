#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#						motors.py						  |
# Drives the motors											  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk & A. Ledesma (monkeeyman@hotmail.co.uk)                       |
#---------------------------------------------------------------------------------------------------------+

import RPi.GPIO as GPIO
from termcolor import colored
import time, comms

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
Pin1 = 22  # right 1, gp pin 25, no 22
Pin2 = 18  # right 2, gp pin 24, no 18
Pin3 = 12  # left 1, gp pin 18, no 12
Pin4 = 16  # left 2, gp pin 23, no 16
GPIO.setup(Pin1, GPIO.OUT)
GPIO.setup(Pin2, GPIO.OUT)
GPIO.setup(Pin3, GPIO.OUT)
GPIO.setup(Pin4, GPIO.OUT)

def drive(pin,state):
        GPIO.output(pin,state)

def stop():
        drive(Pin1, False)
        drive(Pin2, False)
        drive(Pin3, False)
        drive(Pin4, False)

def forwards():
	drive(Pin1, True)
	drive(Pin2, False)
	drive(Pin3, True)
	drive(Pin4, False)

def backwards():
	drive(Pin1, False)
	drive(Pin2, True)
	drive(Pin3, False)
	drive(Pin4, True)

def right():
	drive(Pin1, True)
        drive(Pin2, False)
        drive(Pin3, False)
        drive(Pin4, True)

def left():
	drive(Pin1, False)
	drive(Pin2, True)
	drive(Pin3, True)
	drive(Pin4, False)

stop()
time.sleep(2)
left()
time.sleep(2)
right()
time.sleep(2)
forwards()
time.sleep(2)
backwards()
time.sleep(2)
stop()

def move(d):
	if (d == "F") or (d == "W"):
		forwards()
		comms.sendToUI("Received Forwards")
		print colored("Received Forwards", 'yellow')

	if (d == "B") or (d == "X"):
		backwards()
                comms.sendToUI("Received Backwards")
                print colored("Received Backwards", 'yellow')

	if (d == "L") or (d == "A"):
		left()
                comms.sendToUI("Received Left")
                print colored("Received Left", 'yellow')

	if (d == "R") or (d == "D"):
		right()
                comms.sendToUI("Received Right")
                print colored("Received Right", 'yellow')

	if (d == "Stop") or (d == "S"):
		stop()
                comms.sendToUI("Received Stop")
                print colored("Received Stop", 'yellow')
