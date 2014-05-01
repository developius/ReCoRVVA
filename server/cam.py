#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                                cam.py							  |
# Handles the camera and pan/tilt servos 		                                                  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

from termcolor import colored
import comms, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

servoNeutral = 7.5
servoBackwards = servoLeft = 12.5
servoForwards = servoRight = 2.5
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
tilt = GPIO.PWM(13,50)
pan = GPIO.PWM(15,50)
pan.start(servoNeutral)
tilt.start(servoNeutral)
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
		pan.ChangeDutyCycle(servoLeft)
	if direction == "pan_right":
		print colored("Panning right", 'yellow')
		comms.sendToUI("Panning right")
		pan.ChangeDutyCycle(servoRight)
	if direction == "pan_center":
		print colored("Panning to center", 'yellow')
		comms.sendToUI("Panning to center")
		pan.ChangeDutyCycle(servoNeutral)
	if direction == "tilt_forwards":
		print colored("Tilting forwards", 'yellow')
		comms.sendToUI("Tiliting forwards")
		tilt.ChangeDutyCycle(servoForwards)
	if direction == "tilt_backwards":
		print colored("Tilting backwards", 'yellow')
		comms.sendToUI("Tiliting backwards")
		tilt.ChangeDutyCycle(servoBackwards)
	if direction == "tilt_up":
		print colored("Tilting to center", 'yellow')
		comms.sendToUI("Tiliting to center")
		tilt.ChangeDutyCycle(servoNeutral)
