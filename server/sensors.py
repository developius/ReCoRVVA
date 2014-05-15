#!/usr/bin/python 
#---------------------------------------------------------------------------------------------------------+
#                                               sensors.py                                                |
# Gets the ping from an ultrasonic sensor and the temperature and humididty from a DHT-11 sensor	  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk) and  B. James (musicboyben@gmail.com)	                  |
#---------------------------------------------------------------------------------------------------------+

#Import the various modules
import threading, time, comms, cam, motors, startup, socket, dhtreader, sys, os, numpy
from termcolor import colored
from itertools import repeat
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

headlights = 7
GPIO.setup(headlights, GPIO.OUT)
GPIO.output(headlights, False)

GPIO.setup(11, GPIO.IN)
status = 0

last3 = deque(maxlen=3)

############################################ Ping sensor thread ###########################################################

class Ping (threading.Thread):
        def run (self):
                while True:
			GPIO.output(trig, False)
			time.sleep(0.25)
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
			avg = round(sum(last3) / len(last3)) # --| which one? avg seems to be more reliable
#			mean = numpy.mean(last3)	     # --|

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
				motors.stop()

############################################ Temperature sensor thread ####################################################


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

class Switch (threading.Thread):
        def run (self):
                global status
                while True:
                        if(GPIO.input(11) == True and status == 0):
                                print("switch ON and recorvva is off - starting ReCoRVVA")
                                status = 1
				times = 3
				while times != 0:
				        GPIO.output(headlights, True)
				        time.sleep(0.25)
				        GPIO.output(headlights, False)
				        time.sleep(0.25)
				        times = times - 1
				startup.start()
                                comms.Comms().start()
                                Ping().start()
                                Temp().start()

                        if(GPIO.input(11) == False and status == 1):
                                print("switch OFF and recorvva on - killing ReCoRVVA")
				status = 0
				times = 5
				while times != 0:
                                        GPIO.output(headlights, True)
                                        time.sleep(0.25)
                                        GPIO.output(headlights, False)
                                        time.sleep(0.25)
                                        times = times - 1
				os.system("for x in `jobs -p`; do sudo kill -9 $x; done; sudo killall python")
                                sys.exit()
