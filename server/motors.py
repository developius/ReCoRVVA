#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#						motors.py						  |
# Drives the motors											  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk & A. Ledesma (monkeeyman@hotmail.co.uk)                       |
#---------------------------------------------------------------------------------------------------------+

import RPi.GPIO as GPIO
from RPi.GPIO import output as drive
from termcolor import colored
import time, comms

# setup the pins!
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Pin1 = 22  # right 1, gp pin 25, no 22
Pin2 = 18  # right 2, gp pin 24, no 18
Pin3 = 12  # left 1, gp pin 18, no 12
Pin4 = 16  # left 2, gp pin 23, no 16
"""Pin1 = 18
Pin2 = 22
Pin3 = 16
Pin4 = 12"""
GPIO.setup(Pin1, GPIO.OUT)
GPIO.setup(Pin2, GPIO.OUT)
GPIO.setup(Pin3, GPIO.OUT)
GPIO.setup(Pin4, GPIO.OUT)

# our drive function
#def drive(pin,state):
#        GPIO.output(pin,state)

def stop(): # our stop function!
        drive(Pin1, False)
        drive(Pin2, False)
        drive(Pin3, False)
        drive(Pin4, False)

def backwards(): # our backwards function!
#	stop()
	drive(Pin1, True)
	drive(Pin2, False)
	drive(Pin3, True)
	drive(Pin4, False)

def forwards(): # our forwards function!
#	stop()
	drive(Pin1, False)
	drive(Pin2, True)
	drive(Pin3, False)
	drive(Pin4, True)

def right(): # our right function!
#	stop()
	drive(Pin1, True)
        drive(Pin2, False)
        drive(Pin3, False)
        drive(Pin4, True)

def left(): # our left function!
#	stop()
	drive(Pin1, False)
	drive(Pin2, True)
	drive(Pin3, True)
	drive(Pin4, False)

def move(d): # this is called from comms when a cmd is received
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
