#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               ping.py                                                   |
# Gets the ping from an ultrasonic sensor and the temperature and humididty from a DHT-11 sensor	  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#       Thanks for contribution to B. James (benji@fxapi.co.uk) and A. Ledesma (monkeeyman@hotmail.co.uk) |
#---------------------------------------------------------------------------------------------------------+

#Import the various modules
import threading, time, comms, motors, socket, dhtreader, sys
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
			avg = round(sum(last3) / len(last3))

			pingfile = open('/var/www/crest/pingfile.txt', 'w')
       			pingfile.write(str(avg))
		        pingfile.close()

                        if distance > 10 or avg > 10:
	#			sys.stdout.write("[PING]  No obstructions: %.1f" % avg + "cms\r")
	#			sys.stdout.flush()
				print colored("[PING]  No obstructions: %.1f" % avg + "cms\r", 'green')
			else:
	#			sys.stdout.write("[PING]  PAY ATTENTION: %.1f" % avg + "cms\r")
	#			sys.stdout.flush()
				print colored("[PING]  PAY ATTENTION: %.1f" % avg + "cms\r", 'red')

class Temp (threading.Thread):
        def run (self):
		print colored("Starting temperature and humidity sensor", 'green')
		while True:
			temphumid = dhtreader.read(tempType, tempPin)
			if temphumid is not None:
				t, h = temphumid
#				sys.stdout.write("\r[DHT]   Temp: {0} *C, Hum: {1} %\r".format(t, h)
#				sys.stdout.flush()
				print colored("[DHT]   Temp: {0} *C, Hum: {1} %\r".format(t, h), 'green')
				dhtfile_t = open('/var/www/crest/dhtfile_t.txt', 'w')
				dhtfile_t.write(str(t) + "*C")
				dhtfile_t.close()
				dhtfile_h = open('/var/www/crest/dhtfile_h.txt', 'w')
				dhtfile_h.write(str(h) + "%")
				dhtfile_h.close()
				if t > 50:
					print colored("TEMPERATURE went above 50*C - help!\r", 'red')
				if h > 50:
					print colored("HUMIDITY went above 50 - it's gonna rain!\r", 'red')
			else:
				time.sleep(3)
