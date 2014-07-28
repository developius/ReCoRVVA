#!/usr/bin/python 
#---------------------------------------------------------------------------------------------------------+
#                                               sensors.py                                                |
# Gets the ping from an ultrasonic sensor and the temperature and humididty from a DHT-11 sensor	  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk) and  B. James (musicboyben@gmail.com)	                  |
#---------------------------------------------------------------------------------------------------------+

#Import the modules needed
# comms for communications
# motors for movement
# dhtreader for the temp/humidity sensor

import threading, time, comms, cam, motors, startup, socket, dhtreader, sys, os, numpy
from termcolor import colored
from itertools import repeat
from collections import deque
import RPi.GPIO as GPIO
from random import randrange

trig = 24 # gpio 7
echo = 26 # gpio 8

tempType = 11 # we have a dht-11 reader
tempPin = 3 # our GPIO pin for the data
dhtreader.init() # start the sensor

# setup the GPIOs
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(tempPin, GPIO.IN)

headlights = 7 # our GPIO pin for the headlights
GPIO.setup(headlights, GPIO.OUT) # make the headlights pin an output
GPIO.output(headlights, False) # turn the headlights off

GPIO.setup(11, GPIO.IN) # input pin for switch
status = 0 # status of the ReCoRVVA

last3 = deque(maxlen=3) # storage for our ping values

############################################ Ping sensor thread ###########################################################

class Ping (threading.Thread):
        def run (self):
	        print colored("Starting ping sensor", 'green')
                while True: # get the ping
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

			last3.append(distance) # add the distance to the storage device
			avg = round(sum(last3) / len(last3))
#			mean = numpy.mean(last3)

			"""# save ping to a file on the webserver for visual representations
			pingfile = open('/var/www/crest/pingfile.txt', 'w')
       			pingfile.write(str(avg))
		        pingfile.close()"""

                        if distance > 10 or avg > 10:
				print colored("[PING]  No obstructions: %.1f" % avg + "cms\r", 'green')
				if comms.test_conn() == True:
                                        comms.sendToUI("[PING]  No obstructions: %.1f" % avg + "cms\r")
			else:
				print colored("[PING]  PAY ATTENTION: %.1f" % avg + "cms\r", 'red')
				motors.stop()
				if comms.test_conn() == True:
                                        comms.sendToUI("[PING]  PAY ATTENTION: %.1f" % avg)

############################################ Temperature sensor thread ####################################################


class Temp (threading.Thread):
        def run (self):
		print colored("Starting temperature and humidity sensor", 'green')
		while True: # get temp/humidity
			temphumid = dhtreader.read(tempType, tempPin)
			while temphumid is not None:
				t, h = temphumid
				print colored("[DHT]   Temp: {0} *C, Hum: {1} %\r".format(t, h), 'green')
				if comms.test_conn() == True:
					comms.sendToUI("[DHT]   Temp: {0} *C, Hum: {1} %\r".format(t, h))

				# save temp to a file on webserver
				dhtfile_t = open('/var/www/crest/dhtfile_t.txt', 'w')
				dhtfile_t.write(str(t) + "*C")
				dhtfile_t.close()

				# save humidity to a file on webserver
				dhtfile_h = open('/var/www/crest/dhtfile_h.txt', 'w')
				dhtfile_h.write(str(h) + "%")
				dhtfile_h.close()

				if t > 50:
					print colored("TEMPERATURE went above 50*C - help!\r", 'red')
					motors.stop()
				if h == 100:
					print colored("HUMIDITY is 100% - it's gonna rain!\r", 'red')
					if comms.test_conn() == True:
						comms.sendToUI("HUMIDITY is 100%  - it's gonna rain!\r")
				time.sleep(1)

############################################# Server switch thread ##########################################################

class Switch (threading.Thread):
        def run (self):
                global status
                while True: # get the switch's status
                        if(GPIO.input(11) == True and status == 0): # if switch is on and ReCoRVVA status is off:
                                print("switch ON and ReCoRVVA is off - starting ReCoRVVA")
                                status = 1
				times = 3
				while times != 0: # flash headlights 3 times
				        GPIO.output(headlights, True)
				        time.sleep(0.25)
				        GPIO.output(headlights, False)
				        time.sleep(0.25)
				        times = times - 1
				startup.start() # start the startup routine

                        if(GPIO.input(11) == False and status == 1): # if switch is off and ReCoRVVA status is on:
                                print("switch OFF and ReCoRVVA on - killing ReCoRVVA")
				status = 0
				times = 5
				while times != 0: # flash headlights 5 times
                                        GPIO.output(headlights, True)
                                        time.sleep(0.25)
                                        GPIO.output(headlights, False)
                                        time.sleep(0.25)
                                        times = times - 1
				os.system("for x in `jobs -p`; do sudo kill -9 $x; done; sudo killall python") # kill everything

