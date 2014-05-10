import recorvva

recorvva.connect()

while True:
	input = raw_input("<CLIENT> ")
	recorvva.send_msg(input)
