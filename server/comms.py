#!/usr/bin/python 
#---------------------------------------------------------------------------------------------------------+
#                                               comms.py                                                  |
# Handles the communication through a Python socket							  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

from socket import *
import sys, select, threading, motors, cam, os
from termcolor import colored

address = ('', 7777)
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
client_socket = ""

CMDS = ["A","L","D","R","W","F","X","B","S","Stop","CamOn","CamOff","pan_left","pan_right","pan_center","tilt_forwards","tilt_backwards","tilt_up","HH","HL"]
authorised_addresses = ["fxapi.home", "fxapi.local", "pimine.home", "pimine.local", "25.110.219.165", "mypi.local", "BenPiOne", "Guspi.local", "Xav'sPad", "snail.local"]

def sendToUI(msg):
	try:
		client_socket.send(msg)
	except Exception, e:
		print("Could not send message: " + str(e))

def test_conn():
	try:
		client_socket.send("")
	except:
		return False
	return True

class Comms (threading.Thread):
        def run (self):
		try:
			server_socket.bind(address)
		except Exception, e:
		        print colored("Address already in use", 'red')
			server_socket.close()
		        sys.exit()

		server_socket.listen(2)

		print colored("Socket ready", 'blue')
#		Console().start()

		while True:
			global client_socket
			client_socket, addr = server_socket.accept()
			client_socket.send("Welcome")
   		        hostIP = addr[0]
                	port = addr[1]

                	try:
                        	host = gethostbyaddr(hostIP)[0]
                	except:
                        	host = hostIP
                	print colored("Got connection from: " + host, 'blue')

			if (host in authorised_addresses):
				pass
			else:	# It's malicious
				print colored("Unauthorised connection attempted - " + str(host) + " - closing their socket", 'red')
				client_socket.close()
				print colored("Socket closed to client", 'red')

			while True:
				try:
        	                        recv_data = client_socket.recv(2048)
        	                except:
                	                recv_data = ""

				if (recv_data in CMDS) == True:
					motors.move(recv_data)
					cam.camera(recv_data) 
					cam.servo(recv_data)
				if recv_data == "":
					pass
				if recv_data == " ":
					pass
				if recv_data not in CMDS: # if it's not any of the above, it's something else and we need to know what
#					print colored("Received: '" + recv_data + "' from '" + str(host) + "'", 'blue')
					pass
