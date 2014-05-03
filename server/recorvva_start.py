import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

while True:
	if(GPIO.input(11) == True):
		print("switch ON")
	else:
		print("switch OFF")
