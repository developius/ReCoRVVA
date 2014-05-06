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
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ipad = ('192.168.1.161',7777)

CMDS = ["A","L","D","R","W","F","X","B","S","Stop","CamOn","CamOff","pan_left","pan_right","pan_center","tilt_forwards","tilt_backwards","tilt_up","HH","HL"]

def iPad(msg):
        server_socket.sendto(msg, ipad)

def sendToUI(msg):
	recv_data, addr = server_socket.recvfrom(2048)
        server_socket.sendto(msg,addr)

class Comms (threading.Thread):
        def run (self):
		try:
			server_socket.bind(address)
		except:
		        print colored("Address already in use", 'red')
			server_socket.close()
		        sys.exit()

		print colored("Socket ready", 'blue')

                while True:
			input = raw_input("<TERMINAL> ")
			if input == "exit":
				os.system("sudo killall python")
			if input == "close":
				server_socket.close()
				sys.exit()
			recv_data, addr = server_socket.recvfrom(2048)
			hostIP = addr[0]
			try:
				host = gethostbyaddr(hostIP)[0]
			except:
				host = hostIP

			port = addr[1]
	#		print("Address: " + str(addr))
	#		print("Host's IP: " + str(hostIP) + ", Hostname: " + str(host) + ", Port: " + str(port))
			if (host == "Xav'sPad" or "BenPiOne" or "Guspi" or "snail" or "localhost" or "fxapi"):
				pass
			else:	# It's malicious
				print colored("Unauthorised connection attempted - " + str(host) + " - closing socket", 'red')
				server_socket.close()
				print colored("Socket closed to everyone", 'red')
				break

			if recv_data == "Client connected":
	          		print colored("Client " + str(host) + " connected - and is friendly", 'red')
				sendToUI("Welcome!")
			if recv_data == "Client disconnected":
				print colored("Client " + str(host) + " disconnected", 'red')
				sendToUI("Goodbye!")
			if (recv_data in CMDS) == True:
				motors.move(recv_data)
				cam.camera(recv_data) 
				cam.servo(recv_data)
			if (recv_data == " "):
				pass

			elif recv_data not in CMDS: # if it's not any of the above, it's something else and we need to know what
				print colored("Received: %s" % recv_data, 'blue') # print out the message
	#                        print colored("Length: %.0f" % len(recv_data), 'blue') # print out the length of the message
	                        print colored("Sender hostname: " + str(host), 'blue') # print out the sender's IP
