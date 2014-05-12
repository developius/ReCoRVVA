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
fxapi = ("fxapi.local", port)
address = 0

client_socket = socket(AF_INET, SOCK_STREAM)

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
		client_socket.connect((fxapi))
	except Exception, e:
		print colored("'" + str(fxapi) + "' as address failed", 'red')
		try:
	                client_socket.connect((vpn))
		except Exception, e:
			print colored("'" + str(vpn) + "' (VPN) as address failed" , 'red')
			print colored("Could not connect to ReCoRVVA",'red')
			client_socket.close()
			return False

                print colored("Connected to ReCoRVVA on " + str(vpn), 'blue')
                address = vpn
		return True

        print colored("Connected to ReCoRVVA on " + str(fxapi), 'blue')
        address = fxapi
	return True
def close():
	print colored("\nDisconnecting from ReCoRVVA", 'blue')
	client_socket.shutdown(0)
	client_socket.close()

def send_msg(msg):
	try:
		client_socket.sendto(msg, address)
		print colored("Sent '%s' to ReCoRVVA" % msg, 'green')
	except Exception, e:
		print colored("Could not send message: " + str(e), 'red')

def get_data():
	data_thread().start()

def stop_data():
	data_thread()._Thread__stop()

class data_thread (threading.Thread):
        def run (self):
		while True:
			try:
				recv_data = client_socket.recv(2048)
				if recv_data != " " and recv_data != "":
					print colored("\n<SERVER> " + recv_data, 'red')
			except Exception, e:
				print colored("Could not get data: " + str(e), 'blue')
