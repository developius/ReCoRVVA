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

pan_var = 1500
tilt_var = 1000

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

def servo(msg):
	global pan_var
	global tilt_var
	if msg == "pan_left":
		pan_var = pan_var + 100
		print colored("Panning left " + pan_var, 'yellow')
		servo_mv(pan, pan_var)
		comms.sendToUI("Panning right")
	if msg == "pan_right":
                pan_var = pan_var - 100
                print colored("Panning right " + pan_var, 'yellow')
                servo_mv(pan, pan_var)
		comms.sendToUI("Panning right")
	if msg == "tilt_down":
                tilt_var = tilt_var + 100
                print colored("Tilt down " + tilt_var, 'yellow')
                servo_mv(tilt, tilt_var)
                comms.sendToUI("Tilt down")
        if msg == "tilt_up":
                tilt_var = tilt_var - 100
                print colored("Tilting up " + tilt_var, 'yellow')
                servo_mv(tilt, tilt_var)
                comms.sendToUI("Tilting up")
