#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               ping.py                                                   |
# Gets the ping from an ultrasonic sensor								  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#       Thanks for contribution to B. James (benji@fxapi.co.uk) and A. Ledesma (monkeeyman@hotmail.co.uk) |
#---------------------------------------------------------------------------------------------------------+

#Import the various modules
import threading, time, comms, motors, socket, dhtreader
from termcolor import colored
from collections import deque
import RPi.GPIO as GPIO
from random import randrange

trig = 24 # gpio 7
echo = 26 # gpio 8

tempType = 11
tempPin = 3
dhtreader.init()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(tempPin, GPIO.IN)

last3 = deque(maxlen=3)

class Ping (threading.Thread):
        def run (self):
		print colored("Sending ping to iPad only", 'green')
                while True:
			GPIO.output(trig, False)
			time.sleep(1)
                        GPIO.output(trig, True)
                        time.sleep(0.00001)
                        GPIO.output(trig, False)
                        while GPIO.input(echo) == 0:
                                signaloff = time.time()
                        while GPIO.input(echo) == 1:
                                signalon = time.time()

                        timepassed = signalon - signaloff

                        distance = timepassed * 17000

			last3.append(distance)
			avg = sum(last3) / len(last3)

#			file = open('/var/www/crest/pingfile.txt', 'w')
#       			file.write(avg)
#		        file.close()

                        if distance > 10 or avg > 10:
                                print colored("\nNo obstructions: %.1f" % avg + "cms", 'green')
				comms.iPad('No obstructions: %d' % avg + 'cms')

                        else:
                                print colored("\nPAY ATTENTION: %.1f" % avg + "cms", 'red')
				comms.iPad('PAY ATTENTION: %d' % avg +'cms')

class Temp (threading.Thread):
        def run (self):
		print colored("Starting temperature and humidity sensor", 'green')
		while True:
			if (dhtreader.read(tempType, tempPin) != "None"):
				print "'None' was not found"
				t, h = dhtreader.read(tempType, tempPin)
				print colored("\nTemp = {0} *C, Hum = {1} %".format(t, h), 'green')
				if t > 50:
					print colored("TEMPERATURE went above 50*C - help!", 'red')
				if h > 50:
					print colored("HUMIDITY went above 50 - it's gonna rain!", 'red')
			time.sleep(3)
