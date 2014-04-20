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

T = "True"
F = "False"
PmPin1 = 10
PmPin2 = 12
SmPin1 = 3
SmPin2 = 5

def drive():
	print(Pm1,Pm2,Sm1,Sm2)
        GPIO.output(PmPin1, Pm1)
        GPIO.output(PmPin2, Pm2)
        GPIO.output(SmPin1, Sm1)
        GPIO.output(SmPin2, Sm2)

def move(d):
	if (d == " "):
		Pm1 = " "
		Pm2 = " "
		Sm1 = " "
		Sm2 = " "

	if (d == "F") or (d == "W"):
		Pm1 = T
		Pm2 = F
		Sm1 = T
		Sm2 = F
		comms.sendToUI("Received Forwards")
		print colored("Received Forwards", 'yellow')

	if (d == "B") or (d == "X"):
                Pm1 = F
                Pm2 = T
                Sm1 = F
                Sm2 = T
                comms.sendToUI("Received Backwards")
                print colored("Received Backwards", 'yellow')

	if (d == "L") or (d == "A"):
                Pm1 = F
                Pm2 = F
                Sm1 = T
                Sm2 = F
                comms.sendToUI("Received Left")
                print colored("Received Left", 'yellow')

	if (d == "R") or (d == "D"):
                Pm1 = F
                Pm2 = T
                Sm1 = F
                Sm2 = F
                comms.sendToUI("Received Right")
                print colored("Received Right", 'yellow')

	if (d == "Stop") or (d == "S"):
                Pm1 = F
                Pm2 = F
                Sm1 = F
                Sm2 = F
                comms.sendToUI("Received Stop - Houston, we have a problem!")
                print colored("Received Stop - Houston, we have a problem!", 'yellow')

	else: # just thinking, would this mean that they stop as soon as they've finished executing the motor
	      # control?!
                Pm1 = F
                Pm2 = F
                Sm1 = F
                Sm2 = F

	return (Pm1,Pm2,Sm1,Sm2)
	drive()

#move(1)
