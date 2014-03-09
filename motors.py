#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#						motors.py						  |
# (c) 2014 A. Ledesma (monkeeyman@hotmail.co.uk)                                                          |
#       Thanks for contribution to B. James (benji@fxapi.co.uk) and F. Anderson (finnian@fxapi.co.uk)	  |
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

def turn():
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

	if (d == "F"):
		Pm1 = T
		Pm2 = F
		Sm1 = T
		Sm2 = F
		comms.sendToUI("Received Forwards")
		print colored("Received Forwards", 'blue')

	if (d == "B"):
                Pm1 = F
                Pm2 = T
                Sm1 = F
                Sm2 = T
                comms.sendToUI("Received Backwards")
                print colored("Received Backwards", 'blue')

	if (d == "L"):
                Pm1 = F
                Pm2 = F
                Sm1 = T
                Sm2 = F
                comms.sendToUI("Received Left")
                print colored("Received Left", 'blue')

	if (d == "R"):
                Pm1 = F
                Pm2 = T
                Sm1 = F
                Sm2 = F
                comms.sendToUI("Received Right")
                print colored("Received Right", 'blue')

	if (d == "Stop"):
                Pm1 = F
                Pm2 = F
                Sm1 = F
                Sm2 = F
                comms.sendToUI("Received Stop - Houston, we have a problem!")
                print colored("Received Stop - Houston, we have a problem!", 'blue')

	else: # just thinking, would this mean that they stop as soon as they've finished executing the motor
	      # control?!
                Pm1 = F
                Pm2 = F
                Sm1 = F
                Sm2 = F

	return (Pm1,Pm2,Sm1,Sm2)
	turn()

#move(1)
