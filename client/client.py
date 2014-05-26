#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               client.py                                                 |
# Test script for communication with the RecoRVVA via a Python socket                                 |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

import recorvva, os

recorvva.connect() # connect to ReCoRVVA!

recorvva.get_data() # let's have the data back from the server :)

while True:
	input = raw_input("<CLIENT> ") # get user's input...
	if input == "exit":
		recorvva.close()
		break
	recorvva.send_msg(input) # ...and send it to the server!

os.system('for x in `jobs -p`; do sudo kill -9 $x; done')
