#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                                cam.py							  |
# Handles the camera and pan/tilt servos 		                                                  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

from termcolor import colored
import comms, os, time
import RPi.GPIO as GPIO
from pigpio import set_servo_pulsewidth as servo_mv
import pigpio

pigpio.start()

pan = 22
tilt = 27

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Neutral = 1500
Backwards = Left = 2500
Forwards = Right = 500
headlights = 7

GPIO.setup(headlights, GPIO.OUT)
GPIO.output(headlights, False)

def camera(status):
	if status == "CamOn":
		print colored("Starting camera stream", 'yellow')
		os.system('./startstream.sh &> /dev/null')
	if status == "CamOff":
		print colored("Stopping camera stream", 'yellow')
		os.system('sudo killall raspistill')
	
	if status == "HL":
		print colored("Switching off headlights", 'yellow')
		GPIO.output(headlights, False)
		comms.sendToUI("Headlights off")

	if status == "HH":
		print colored("Switching on headlights", 'yellow')
		GPIO.output(headlights, True)
		comms.sendToUI("Headlights on")

def servo(direction):
	if direction == "pan_left":
		print colored("Panning left", 'yellow')
		comms.sendToUI("Panning left")
		servo_mv(pan, Left)
	if direction == "pan_right":
		print colored("Panning right", 'yellow')
		comms.sendToUI("Panning right")
		servo_mv(pan, Right)
	if direction == "pan_center":
		print colored("Panning to center", 'yellow')
		comms.sendToUI("Panning to center")
		servo_mv(pan, Neutral)
	if direction == "tilt_forwards":
		print colored("Tilting forwards", 'yellow')
		comms.sendToUI("Tiliting forwards")
		servo_mv(tilt, Forwards)
	if direction == "tilt_backwards":
		print colored("Tilting backwards", 'yellow')
		comms.sendToUI("Tiliting backwards")
		servo_mv(tilt, Backwards)
	if direction == "tilt_up":
		print colored("Tilting to center", 'yellow')
		comms.sendToUI("Tiliting to center")
		servo_mv(tilt, Neutral)
