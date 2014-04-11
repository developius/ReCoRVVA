#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#						test_temp.py				                  |
# Takes a reading from the DHT-11 temperature sensor                                                      |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk) and B. James (musicboyben1999@gmail.com)                     |
#---------------------------------------------------------------------------------------------------------+


import dhtreader

type = 11
pin = 3

dhtreader.init()
print dhtreader.read(type, pin)
