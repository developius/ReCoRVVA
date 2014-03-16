#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               recorvva.py                                               |
# API for communication with the RecoRVVA via a Python socket						  |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

from socket import *
from time import sleep
from termcolor import colored
import sys, threading

address = ('fxapi', 7777)
client_socket = socket(AF_INET, SOCK_DGRAM)

def help():
	print colored("ReCoRVVA - Remote Controlled Robot Vehicle for Various Applications: help", 'blue')
	print colored("help()		- guess", 'yellow')
	print colored("api_version()	- again, guess", 'yellow')
	print colored("connect()	- connect to ReCoRVVA", 'yellow')
	print colored("close()		- disconnect from ReCoRVVA", 'yellow')
	print colored('send_msg("txt")	- send "text" to the ReCoRVVA', 'yellow')
	print colored("get_data()       - get the server output", 'yellow')
	print colored("stop_data()	- stops the data outpyt", 'yellow')

def api_version():
	print colored("The API version is '1'", 'blue')

def connect():
	print colored("Connecting to ReCoRVVA", 'blue')
	client_socket.connect(address)
	client_socket.sendto("Client connected", address)
	client_socket.sendto(" ", address)

def close():
	print colored("\nDisconnecting from ReCoRVVA", 'blue')
	send_msg("Client disconnected", address)
	stop_data()
	client_socket.close()

def send_msg(msg):
	print colored("Sending '%s' to ReCoRVVA" % msg, 'green')
	client_socket.sendto(msg, address)
	client_socket.sendto(" ", address) #need to send two things for it to work

def get_data():
	data_thread().start()

def stop_data():
	data_thread()._Thread__stop()

class data_thread (threading.Thread):
        def run (self):
		while True:
			recv_data, addr = client_socket.recvfrom(2048)
			print colored("\n<SERVER> " + recv_data, 'red')
