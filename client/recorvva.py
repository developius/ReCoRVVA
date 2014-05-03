#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               recorvva.py                                               |
# API and wrapper for communication with the RecoRVVA via a Python socket						  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+
  
from socket import *
from time import sleep
from termcolor import colored
import sys, threading

port = 7777
vpn = ("25.110.219.165", port)
fxapi = ("fxapi", port)
fxapiL = ("fxapi.local", port)
address = 0

client_socket = socket(AF_INET, SOCK_DGRAM)

def help():
	print colored("ReCoRVVA - Remote Controlled Robot Vehicle for Various Applications: help", 'blue')
	print colored("Function:	- Description", 'red')
	print colored("help()		- prints this help", 'yellow')
	print colored("api_version()	- prints API version", 'yellow')
	print colored("connect()	- connect to ReCoRVVA", 'yellow')
	print colored("close()		- disconnect from ReCoRVVA", 'yellow')
	print colored('send_msg("txt")	- send "text" to the ReCoRVVA', 'yellow')
	print colored("get_data()       - get the server output", 'yellow')
	print colored("stop_data()	- stops the data output", 'yellow')

def api_version():
	print colored("The API version is '1'", 'blue')

def commands():
	print colored("Valid commands:", 'red')
	print colored("A/L 		Left", 'blue')
	print colored("D/R 		Right", 'blue')
	print colored("W/F 		Forwards", 'blue')
	print colored("X/B		Backwards", 'blue')
	print colored("Stop 		Stop", 'blue')
	print colored("CamOn		Turn on camera", 'blue')
	print colored("CamOff		Turn off camera", 'blue')
	print colored("pan_left	Pan camera left", 'blue')
	print colored("pan_right	Pan camera right", 'blue')
	print colored("pan_center	Pan camera to center", 'blue')
	print colored("tilt_forwards	Tilt the camera forwards", 'blue')
	print colored("tilt_backwards	Tilt the camera backwards", 'blue')
	print colored("tilt_up   	Tilt camera up", 'blue')
	print colored("HH		Turn headlights on", 'blue')
	print colored("HL		Turn headlights off", 'blue')

def connect():
	global address
	try:
		client_socket.connect((vpn))
		client_socket.sendto("Client connected", vpn)
		client_socket.sendto(" ", vpn)
	except:
		print colored("'VPN' as address failed", 'red')
		try:
	                client_socket.connect((fxapiL))
        	        client_socket.sendto("Client connected", fxapiL)
			client_socket.sendto(" ", fxapiL)
		except:
			print colored("'fxapi.local' as address failed", 'red')
			try:
		                client_socket.connect((fxapi))
		                client_socket.sendto("Client connected", fxapi)
				client_socket.sendto(" ", fxapi)
			except:
				print colored("'25.110.219.165' (VPN) as address failed", 'red')
				print colored("Could not connect to ReCoRVVA",'red')
				sys.exit(0)

			print colored("Connected to ReCoRVVA on " + str(fxapi), 'blue')
	                address = fxapi

		print colored("Connected to ReCoRVVA on " + str(fxapiL), 'blue')
                address = fxapiL

	print colored("Connected to ReCoRVVA on " + str(vpn), 'blue')
	address = vpn

def close():
	print colored("\nDisconnecting from ReCoRVVA", 'blue')
	send_msg("Client disconnected")
#	stop_data()
	client_socket.shutdown(0)
	client_socket.close()

def send_msg(msg):
	try:
		client_socket.sendto(msg, address)
		client_socket.sendto(" ", address) #need to send two things for it to work
		print colored("Sent '%s' to ReCoRVVA" % msg, 'green')
	except error:
		print colored("Could not send message", 'blue')
#		sys.exit(1)

def get_data():
	data_thread().start()

def stop_data():
	data_thread()._Thread__stop()

class data_thread (threading.Thread):
        def run (self):
		while True:
			try:
				recv_data, addr = client_socket.recvfrom(2048)
				print colored("\n<SERVER> " + recv_data, 'red')
			except error:
				print colored("Could not get data", 'blue')
