import sys
import mysql.connector
import RPi.GPIO as GPIO
import functions as fu
import json
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

decoded_data = json.loads(sys.argv[1])
phase1 = decoded_data[0]['phase1']


for i in range(len(decoded_data)):
	phase1 = decoded_data[i]['phase1']
	phase2 = decoded_data[i]['phase2']
	phase3 = decoded_data[i]['phase3']
	time = decoded_data[i]['time']
	if phase1 == '0':
		fu.send_gpio(1,0)
	if phase1 == '1':
		fu.send_gpio(1,1)
	if phase1 == '2':
		fu.send_gpio(1,2)
	if phase1 == '3':
		fu.send_gpio(1,3)
	if phase1 == '4':
		fu.send_gpio(1,4)
	if phase1 == '5':
		fu.send_gpio(1,5)
	if phase1 == '6':
		fu.send_gpio(1,6)
	if phase2 == '0':
		fu.send_gpio(2,0)
	if phase2 == '1':
		fu.send_gpio(2,1)
	if phase2 == '2':
		fu.send_gpio(2,2)
	if phase2 == '3':
		fu.send_gpio(2,3)
	if phase2 == '4':
		fu.send_gpio(2,4)
	if phase2 == '5':
		fu.send_gpio(2,5)
	if phase2 == '6':
		fu.send_gpio(2,6)
	if phase3 == '0':
		fu.send_gpio(3,0)
	if phase3 == '1':
		fu.send_gpio(3,1)
	if phase3 == '2':
		fu.send_gpio(3,2)
	if phase3 == '3':
		fu.send_gpio(3,3)
	if phase3 == '4':
		fu.send_gpio(3,4)
	if phase3 == '5':
		fu.send_gpio(3,5)
	if phase3 == '6':
		fu.send_gpio(3,6)
	fu.conx_send_all(phase1,phase2,phase3)
	sleep(int(time))
else:
	fu.send_gpio(1,0)
	fu.send_gpio(2,0)
	fu.send_gpio(3,0)
	fu.conx_send_all("0","0","0")
