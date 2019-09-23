## This file enables the GPIOS when the user choose phase and position from web.
## The reason why functions file is not used is because of the time response:
## this way take less time to respond.

#Libraries
#coding: utf-8
import sys
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

#Info coming from send.php
position = sys.argv[1]
phase = sys.argv[2]

#####This is another option to make this easier. However, the time response is higher.
###import functions as fu
###fu.send_gpio(int(phase),int(position))
#Note: line 16 in file send.php must be modified to shell_exec("python3 /var/www/html/send.py '".$position."' '".$phase."'")


#SET OUTPUTS with the info conming from send.php;
if phase == "1":
	if position == "0":
		GPIO.output(14,True)
		GPIO.output(15,True)
		GPIO.output(18,True)
	elif position == "1":
		GPIO.output(14,False)
		GPIO.output(15,True)
		GPIO.output(18,True)
	elif position == "2":
		GPIO.output(14,True)
		GPIO.output(15,False)
		GPIO.output(18,True)
	elif position == "3":
		GPIO.output(14,True)
		GPIO.output(15,True)
		GPIO.output(18,False)
	elif position == "4":
		GPIO.output(14,False)
		GPIO.output(15,True)
		GPIO.output(18,False)
	elif position == "5":
		GPIO.output(14,True)
		GPIO.output(15,False)
		GPIO.output(18,False)
	elif position == "6":
		GPIO.output(14,False)
		GPIO.output(15,False)
		GPIO.output(18,False)
elif phase == "2":
	if position == "0":
		GPIO.output(23,True)
		GPIO.output(24,True)
		GPIO.output(25,True)
	elif position == "1":
		GPIO.output(23,False)
		GPIO.output(24,True)
		GPIO.output(25,True)
	elif position == "2":
		GPIO.output(23,True)
		GPIO.output(24,False)
		GPIO.output(25,True)
	elif position == "3":
		GPIO.output(23,True)
		GPIO.output(24,True)
		GPIO.output(25,False)
	elif position == "4":
		GPIO.output(23,False)
		GPIO.output(24,True)
		GPIO.output(25,False)
	elif position == "5":
		GPIO.output(23,True)
		GPIO.output(24,False)
		GPIO.output(25,False)
	elif position == "6":
		GPIO.output(23,False)
		GPIO.output(24,False)
		GPIO.output(25,False)
elif phase == "3":
	if position == "0":
		GPIO.output(17,True)
		GPIO.output(27,True)
		GPIO.output(22,True)
	elif position == "1":
		GPIO.output(17,False)
		GPIO.output(27,True)
		GPIO.output(22,True)
	elif position == "2":
		GPIO.output(17,True)
		GPIO.output(27,False)
		GPIO.output(22,True)
	elif position == "3":
		GPIO.output(17,True)
		GPIO.output(27,True)
		GPIO.output(22,False)
	elif position == "4":
		GPIO.output(17,False)
		GPIO.output(27,True)
		GPIO.output(22,False)
	elif position == "5":
		GPIO.output(17,True)
		GPIO.output(27,False)
		GPIO.output(22,False)
	elif position == "6":
		GPIO.output(17,False)
		GPIO.output(27,False)
		GPIO.output(22,False)
