#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               client.py                                                 |
# Test script for communication with the RecoRVVA via a Python socket                                 |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

import recorvva

recorvva.connect()

while True:
	input = raw_input("<CLIENT> ")
	if input == "exit":
		break
	recorvva.send_msg(input)

recorvva.close()
