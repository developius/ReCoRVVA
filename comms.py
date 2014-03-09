#!/usr/bin/python
#----------------------------------------------------------------------------------------------------------+
#                                               comms.py                                                  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#       Thanks for contribution to B. James (benji@fxapi.co.uk) and A. Ledesma (monkeeyman@hotmail.co.uk) |
#---------------------------------------------------------------------------------------------------------+

from socket import *
import sys, select, threading, motors
from termcolor import colored

address = ('0.0.0.0', 7777)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

ipad = ('192.168.1.161',7777)

CMDS = ["L","R","F","B","Stop","CamOn","CamOff"]

def iPad(msg):
        server_socket.sendto(msg, ipad)

def sendToUI(msg):
	recv_data, addr = server_socket.recvfrom(2048)
        server_socket.sendto(msg,addr)

class Comms (threading.Thread):
        def run (self):
		print colored("Listening", 'red')
                while True:
			recv_data, addr = server_socket.recvfrom(2048)
			addr = str(addr)
			if recv_data == "Client connected" :
				print colored("Client " + addr + " connected", 'red')
				sendToUI("Welcome!")
				iPad("Client " + addr + " connected")
			if recv_data == "Client disconnected":
				print colored("Client " + addr + " disconnected", 'red')
				sendToUI("Goodbye!")
				iPad("Client " + addr + " disconnected")
			elif recv_data != "Client connected" or recv_data != "Client connected" or not recv_data in CMDS: # if preset cmds or client con/discon
				print colored("Received: %s" % recv_data, 'blue') # print out the message
	#                        print colored("Length: %.0f" % len(recv_data), 'blue') # print out the length of the message
	                        print colored("Sender IP: " + addr, 'blue') # print out the sender's IP

			# check if for cam or motors

			motors.move(recv_data) # send the message to motors for direction checking
           	        #cam.camera(recv_data) # send the message to camera for pan/tilt
#                       sendToUI(recv_data) #sends the original message back to UI
