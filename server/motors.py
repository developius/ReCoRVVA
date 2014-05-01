#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#						motors.py						  |
# Drives the motors
# (c) 2014 A. Ledesma (monkeeyman@hotmail.co.uk)                                                          |
#---------------------------------------------------------------------------------------------------------+

import RPi.GPIO as GPIO
from termcolor import colored
import time
import comms

GPIO.setmode(GPIO.BOARD)
T = "True"
F = "False"
Pin1 = 22  # right 1, pin 25, turn left (forwards)
Pin2 = 18  # right 2, pin 24, turn left (backwards)
Pin3 = 12  # left 1, pin 18, turn right (backwards)
Pin4 = 16  # left 2, pin 23, turn right (forwards)
GPIO.setup(Pin1, GPIO.OUT)
GPIO.setup(Pin2, GPIO.OUT)
GPIO.setup(Pin3, GPIO.OUT)
GPIO.setup(Pin4, GPIO.OUT)

def drive(pin,state):
        GPIO.output(pin,state)

def left():
	drive(Pin1, True)
	drive(Pin2, False)
	drive(Pin3, False)
	drive(Pin4, False)

def right():
	drive(Pin1, False)
	drive(Pin2, False)
	drive(Pin3, False)
	drive(Pin4, True)

def forwards():
	drive(Pin1, True)
        drive(Pin2, False)
        drive(Pin3, False)
        drive(Pin4, True)

def backwards():
	drive(Pin1, False)
	drive(Pin2, True)
	drive(Pin3, True)
	drive(Pin4, False)

def stop():
	drive(Pin1, False)
        drive(Pin2, False)
        drive(Pin3, False)
        drive(Pin4, False)

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
                comms.sendToUI("Received Stop - Houston, we have a problem!")
                print colored("Received Stop - Houston, we have a problem!", 'yellow')
