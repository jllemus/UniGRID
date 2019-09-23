#Libraries
import sys
import RPi.GPIO as GPIO

#GPIO initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

#Getting information coming from reset.php
sw = sys.argv[1]

#Turning off all GPIOs
if sw == "1":
	GPIO.output(14,True)
	GPIO.output(15,True)
	GPIO.output(18,True)
	GPIO.output(17,True)
	GPIO.output(27,True)
	GPIO.output(22,True)
	GPIO.output(23,True)
	GPIO.output(24,True)
	GPIO.output(25,True)
