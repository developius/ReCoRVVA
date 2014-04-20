#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               xbox.py                                                   |
# API and wrapper for communication with the RecoRVVA via a Python socket                                 |
# (c) 2014 A. Ledesma (monkeeyman@hotmail.co.uk)                                                          |
#---------------------------------------------------------------------------------------------------------+

import socket, recorvva

recorvva.connect()

while True:
	input = raw_input("Type the message you want to send: ")
	print("Sending: " + input)
	recorvva.send_msg(input)

