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

servoNeutral = 7.5
servoUp = servoRight = 12.5
servoDown = servoLeft = 2.5
#pan = GPIO.PWM(24,50)
#tilt = GPIO.PWM(26,50)
#pan.start(servoNeutral)
#tilt.start(servoNeutral)
headlights = 7

GPIO.setup(headlights, GPIO.OUT)

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
		#comms.sendToUI("Headlights off")

	if status == "HH":
		print colored("Switching on headlights", 'yellow')
		GPIO.output(headlights, True)
		#comms.sendToUI("Headlights on")

def servo(direction):
	if direction == "pan_left":
		print colored("Panning left", 'yellow')
		comms.sendToUI("Panning left")
#       	pan.ChangeDutyCycle(servoLeft)
	if direction == "pan_right":
		print colored("Panning right", 'yellow')
		comms.sendToUI("Panning right")
#		pan.ChangeDutyCycle(servoRight)
	if direction == "pan_neutral":
		print colored("Panning to neutral", 'yellow')
		comms.sendToUI("Panning to neutral")
#		pan.ChangeDutyCycle(servoNeutral)
	if direction == "tilt_down":
		print colored("Tilting down", 'yellow')
		comms.sendToUI("Tiliting down")
#		tilt.ChangeDutyCycle(servoDown)
	if direction == "tilt_up":
		print colored("Tilting up", 'yellow')
		comms.sendToUI("Tiliting up")
#		tilt.ChangeDutyCycle(servoUp)
	if direction == "tilt_neutral":
		print colored("Tilting to neutral", 'yellow')
		comms.sendToUI("Tiliting to neutral")
#		tilt.ChangeDutyCycle(servoNeutral)
