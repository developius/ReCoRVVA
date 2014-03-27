#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               comms.py                                                  |
# Handles the communication through a Python socket							  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#       Thanks for contribution to B. James (benji@fxapi.co.uk) and A. Ledesma (monkeeyman@hotmail.co.uk) |
#---------------------------------------------------------------------------------------------------------+

from socket import *
import sys, select, threading, motors, cam
from termcolor import colored

address = ('0.0.0.0', 7777)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

ipad = ('192.168.1.161',7777)

CMDS = ["A","L","D","R","W","F","X","B","S","Stop","CamOn","CamOff","pan_left","pan_right","pan_neutral","tilt_up","tilt_down","tilt_neutral","HH","HL"]

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
			if (recv_data in CMDS) == True:
				motors.move(recv_data)
				cam.camera(recv_data)
				cam.servo(recv_data)
			
			else: # if it's not any of the above, it's something else and we need to know what
				print colored("Received: %s" % recv_data, 'blue') # print out the message
	#                        print colored("Length: %.0f" % len(recv_data), 'blue') # print out the length of the message
	                        print colored("Sender IP: " + addr, 'blue') # print out the sender's IP
