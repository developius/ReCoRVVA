#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               ping.py                                                   |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#       Thanks for contribution to B. James (benji@fxapi.co.uk) and A. Ledesma (monkeeyman@hotmail.co.uk) |
#---------------------------------------------------------------------------------------------------------+

#Import the various modules
import threading, time, comms, motors, socket
from termcolor import colored
from collections import deque
import RPi.GPIO as GPIO

last3 = deque(maxlen=3)

class Ping (threading.Thread):
        def run (self):
		print colored("Sending ping to iPad only", 'green')
                while True:
			GPIO.output(7,GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(7,True)
                        time.sleep(0.00001)
                        GPIO.output(7,False)
                        while GPIO.input(8) == 0:
                                signaloff = time.time()

                        while GPIO.input(8) == 1:
                                signalon = time.time()

                        timepassed = signalon - signaloff

                        distance = timepassed * 17000
                        distance4term = round(timepassed * 17000, 2)
                        distance4cli = round(timepassed * 17000, 10)

			last3.append(distance)
			avg = sum(last3) / len(last3)

                        if distance >= 10 or avg >= 10:
                                print colored("No obstructions: %.1f" % distance4term + "cms", 'green')
				comms.iPad('No obstructions: %d' % avg + 'cms')

                        else:
                                print colored("PAY ATTENTION: %.1f" % distance4term + "cms", 'red')
				comms.iPad('PAY ATTENTION: %d' % avg +'cms')
