#!/usr/bin/python 
#---------------------------------------------------------------------------------------------------------+
#                                               comms.py                                                  |
# Handles the communication through a Python socket							  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

from socket import *
import sys, select, threading, motors, cam, os
from termcolor import colored

# define our address ('' means all available addresses) and port (7777)
address = ('', 7777)
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# client_socket var is empty
client_socket = None

# available commands
CMDS = ["A","L","D","R","W","F","X","B","S","Stop","CamOn","CamOff","pan_left","pan_right","pan_center","tilt_forwards","tilt_backwards","tilt_up","HH","HL"]
# what it says on the tin
authorised_addresses = ["fxapi.home", "fxapi.local", "pimine.home", "pimine.local", "25.110.219.165", "Xav'sPad", "snail.local"]

def sendToUI(msg): # function for sending to client's socket
	if client_socket is not None:
		try:
			client_socket.send(msg)
		except Exception, e:
			print("Could not send message: " + str(e))

def test_conn(): # function for testing the connection
	try:
		client_socket.recv()
	except:
		return False
	return True

class Comms (threading.Thread):
        def run (self):
		global server_socket
		try: # to bind the address
			server_socket.bind(address)
		except Exception, e:
		        print colored("Address already in use: " + str(e), 'red')
			server_socket.shutdown(1)
			server_socket.close()
			os.system('sudo killall -9 python')
			
		server_socket.listen(2) # listen for max 2 clients

		print colored("Socket ready", 'blue')
		global client_socket

		while True:
			client_socket, addr = server_socket.accept() # when connection received, split it into socket addr and internet addr
   		        hostIP = addr[0] # get the host's ip
                	port = addr[1] # get the host's port

                	try: # try to get the hostname from the ip
                        	host = gethostbyaddr(hostIP)[0]
                	except: # do our best
                        	host = hostIP
                	print colored("Got connection from: " + host, 'blue')

			if (host not in authorised_addresses): # test to see if it's an authorised connection
				print colored("Unauthorised connection attempted - " + str(host) + " - closing their socket", 'red')
				client_socket.send("You are not authorised to connect - sorry. Go die in a hole.")
				client_socket.close() # close their socket
				client_socket = None

			if client_socket is not None: # if they ARE authorised...
				client_socket.send("Welcome") # ...welcome them!

				while True:
					if client_socket is not None:
	        	                        recv_data = client_socket.recv(2048) # get data
						if not recv_data: #or client_socket.recv(1024) == 0:
							print colored("Client %s disconnected" % host, 'red')
							client_socket.close()
			                                break

						if (recv_data in CMDS) == True: # if it's a command
							motors.move(recv_data) # tell the motors what it is
							cam.camera(recv_data) # tell the camera what it is
							cam.servo(recv_data)

						if recv_data == "":
							pass
						if recv_data == " ":
							pass

						if recv_data not in CMDS: # if it's not any of the above, it's something else and we may need to know what
#							print colored("Received: '" + recv_data + "' from '" + str(host) + "'", 'blue')
							pass
			elif client_socket is None: #or test_conn == False:
                                print colored("Client %s disconnected" % host, 'red')
