import socket, recorvva

recorvva.connect()

while True:
	input = raw_input("Type the message you want to send: ")
	print("Sending: " + input)
	recorvva.send_msg(input)

