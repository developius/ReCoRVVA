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

pigpio.start() # start pigpio

pan = 22 # pan servo pin
tilt = 27 # tilt servo pin

pan_var = 1500 # initially, pan centre
tilt_var = 1000 # initially, tilt forwards

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Neutral = 1500
Backwards = Left = 2500
Forwards = Right = 500
headlights = 7

GPIO.setup(headlights, GPIO.OUT)
GPIO.output(headlights, False)

def camera(status): # gets called from comms when data is received
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

def servo(msg):
	global pan_var
	global tilt_var
	if msg == "pan_left":
		pan_var = pan_var + 100
		if pan_var < 2500 and pan_var > 500:
			print colored("Panning left " + str(pan_var), 'yellow')
			servo_mv(pan, pan_var) # pan left a bit
			comms.sendToUI("Panning left")
		else: # to stop trying to pan too far
			pan_var = pan_var - 100

	if msg == "pan_right":
		pan_var = pan_var - 100
		if pan_var < 2500 and pan_var > 500:
	                print colored("Panning right " + str(pan_var), 'yellow')
	                servo_mv(pan, pan_var) # pan right a bit
			comms.sendToUI("Panning right")
		else: # to stop trying to pan too far
                        pan_var = pan_var + 100

	if msg == "tilt_backwards":
		tilt_var = tilt_var + 100
		if tilt_var < 2500 and tilt_var > 500:
	                print colored("Tilting backwards " + str(tilt_var), 'yellow')
	                servo_mv(tilt, tilt_var) # tilt backwards a bit
	                comms.sendToUI("Tilting backwards")
		else: # to stop tilting too far
                        tilt_var = tilt_var + 100

        if msg == "tilt_forwards":
		tilt_var = tilt_var - 100
		if tilt_var < 2500 and tilt_var > 500:
	                print colored("Tilting forwards " + str(tilt_var), 'yellow')
	                servo_mv(tilt, tilt_var) # tilt forwards a bit
	                comms.sendToUI("Tilting forwards")
		else:
                        tilt_var = tilt_var + 100
