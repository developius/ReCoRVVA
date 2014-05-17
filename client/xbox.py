#!/usr/bin/python 
#---------------------------------------------------------------------------------------------------------+
#                                               xbox.py                                                   |
# API and wrapper for communication with the RecoRVVA via a Python socket                                 |
# (c) 2014 A. Ledesma (monkeeyman@hotmail.co.uk)                                                          |
#---------------------------------------------------------------------------------------------------------+

import socket, recorvva, threading
from termcolor import colored
from legopi.lib import xbox_read

recorvva.connect()

class Xbox (threading.Thread):
	def run (self):
		for event in xbox_read.event_stream(deadzone=12000):
                        event = event.replace("Event", "")
			event = str(event)
			print colored(event,'red')
			if event == "(Y,1,0)":
				print("you pressed Y")
				recorvva.send_msg("you pressed Y")
			if event == "(Y,0,1)":
				print("you released Y")
				recorvva.send_msg("you released Y")
			if event == "(X,1,0)":
                                print("you pressed X")
                                recorvva.send_msg("you pressed X")
                        if event == "(X,0,1)":
                                print("you released X")
                                recorvva.send_msg("you released X")
			if event == "(A,1,0)":
                                print("you pressed A")
                                recorvva.send_msg("you pressed A")
                        if event == "(A,0,1)":
                                print("you released A")
                                recorvva.send_msg("you released A")
			if event == "(B,1,0)":
                                print("you pressed B")
                                recorvva.send_msg("you pressed B")
                        if event == "(B,0,1)":
                                print("you released B")
                                recorvva.send_msg("you released B")
			if event == "(RB,1,0)":
                                print("you pressed RB")
                                recorvva.send_msg("you pressed RB")
                        if event == "(RB,0,1)":
                                print("you released RB")
                                recorvva.send_msg("you released RB")
			if event == "(LB,1,0)":
                                print("you pressed LB")
                                recorvva.send_msg("you pressed LB")
                        if event == "(LB,0,1)":
                                print("you released LB")
                                recorvva.send_msg("you released LB")
			if event == "(dr,1,0)":
                                print("you pressed dr")
                                recorvva.send_msg("you pressed dr")
                        if event == "(dr,0,1)":
                                print("you released dr")
                                recorvva.send_msg("you released dr")
			if event == "(du,1,0)":
                                print("you pressed du")
                                recorvva.send_msg("you pressed du")
                        if event == "(du,0,1)":
                                print("you released du")
                                recorvva.send_msg("you released du")
			if event == "(dl,1,0)":
                                print("you pressed dl")
                                recorvva.send_msg("you pressed dl")
                        if event == "(dl,0,1)":
                                print("you released dl")
                                recorvva.send_msg("you released dl")
			if event == "(dd,1,0)":
                                print("you pressed dd")
                                recorvva.send_msg("you pressed dd")
                        if event == "(dd,0,1)":
                                print("you released dd")
                                recorvva.send_msg("you released dd")
			if event == "(TL,1,0)":
                                print("you pressed TL")
                                recorvva.send_msg("you pressed TL")
                        if event == "(TL,0,1)":
                                print("you released TL")
                                recorvva.send_msg("you released TL")
			if event == "(TR,1,0)":
                                print("you pressed TR")
                                recorvva.send_msg("you pressed TR")
                        if event == "(TR,0,1)":
                                print("you released TR")
                                recorvva.send_msg("you released TR")
			if event == "(back,1,0)":
                                print("you pressed back")
                                recorvva.send_msg("you pressed back")
                        if event == "(back,0,1)":
                                print("you released back")
                                recorvva.send_msg("you released back")
			if event == "(start,1,0)":
                                print("you pressed start")
                                recorvva.send_msg("you pressed start")
                        if event == "(start,0,1)":
                                print("you released start")
                                recorvva.send_msg("you released start")
			if event == "(guide,1,0)":
                                print("you pressed guide")
                                recorvva.send_msg("you pressed guide")
                        if event == "(guide,0,1)":
                                print("you released guide")
                                recorvva.send_msg("you released guide")
			if event == "(RT,1,0)":
                                print("you pressed RT")
                                recorvva.send_msg("you pressed RT")
                        if event == "(RT,0,1)":
                                print("you released RT")
                                recorvva.send_msg("you released RT")

Xbox().start()

while True:
	input = raw_input("Type the message you want to send: ")
	print("Sending: " + input)
	recorvva.send_msg(input)

