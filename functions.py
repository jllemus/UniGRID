#FUNCTIONS FILE

#coding: utf-8
#Libraries
import RPi.GPIO as GPIO
import mysql.connector
import time

#GPIO initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

def pul():
	"""
		This function allows to use GPIO 4 and GPIO 9 as inputs. Once this function
		is called the variables phase and position_pos will return a boolean value.
	"""
	phase = GPIO.input(4)
	position_pos = GPIO.input(9)
	return phase,position_pos

def conx_send(phase,position):
	"""
		This function makes a database connection and updates all the information in the 
		individually. That means, when the function is called, just the selected phase
		will be updated
	"""
	res_val = res(position)
	con = mysql.connector.connect(host = "localhost",user = "jose5",password = "12345", database = "database", autocommit = True)
	cursor = con.cursor()
	cursor.execute("UPDATE info2 SET phase"+str(phase)+"='"+str(position)+"',res"+str(phase)+"='"+res_val+"'")
	cursor.close()
	con.close()

def conx_ret():
	"""
		This function makes a database connection to retrieve the information: position in each phase 
		and also the control value.
	"""
	con = mysql.connector.connect(host = "localhost", user = "jose5",password = "12345", database = "database")
	cursor = con.cursor()
	cursor.execute("SELECT control,phase1,phase2,phase3 FROM info2")
	rows = cursor.fetchall()
	for row in rows:
		control=str(row)[1]
		phase1 = str(row)[4]
		phase2 = str(row)[7]
		phase3 = str(row)[10]
	return control,phase1,phase2,phase3
	cursor.close()
	con.close()

def conx_send_all(phase1,phase2,phase3):
	"""
		This function makes a database connection and, unlike conx_send, updates ALL THE INFORMATION. 
	"""
	res1 = res(int(phase1))
	res2 = res(int(phase2))
	res3 = res(int(phase3))
	con = mysql.connector.connect(host = "localhost",user = 'jose5', password = '12345', database = 'database',autocommit = True)
	cursor = con.cursor()
	cursor.execute("UPDATE info2 SET phase1 = '"+str(phase1)+"', phase2 = '"+str(phase2)+"',phase3 = '"+str(phase3)+"', res1 = '"+res1+"', res2 = '"+res2+"', res3 = '"+res3+"'")

def res(val):
	"""
		This function assign the resistance value to each position in the resistance module.
	"""
	if val == 0:
		pos = "∞"
	if val == 1:
		pos = "240"
	if val == 2:
		pos = "120"
	if val == 3:
		pos = "80"
	if val == 4:
		pos = "60"
	if val == 5:
		pos = "48"
	if val == 6:
		pos = "40"
	return pos

def send_gpio(phase,position):
	"""
		Function to define which GPIO pin should be enabled to get phase and position in the
		resistance module.
	"""
	if phase == 1:
		if position == 0:
			GPIO.output(14,True)
			GPIO.output(15,True)
			GPIO.output(18,True)
		if position == 1:
			GPIO.output(14,False)
			GPIO.output(15,True)
			GPIO.output(18,True)
		if position == 2:
			GPIO.output(14,True)
			GPIO.output(15,False)
			GPIO.output(18,True)
		if position == 3:
			GPIO.output(14,True)
			GPIO.output(15,True)
			GPIO.output(18,False)
		if position == 4:
			GPIO.output(14,False)
			GPIO.output(15,True)
			GPIO.output(18,False)
		if position == 5:
			GPIO.output(14,True)
			GPIO.output(15,False)
			GPIO.output(18,False)
		if position == 6:
			GPIO.output(14,False)
			GPIO.output(15,False)
			GPIO.output(18,False)
	if phase == 2:
		if position == 0:
			GPIO.output(23,True)
			GPIO.output(24,True)
			GPIO.output(25,True)
		if position == 1:
			GPIO.output(23,False)
			GPIO.output(24,True)
			GPIO.output(25,True)
		if position == 2:
			GPIO.output(23,True)
			GPIO.output(24,False)
			GPIO.output(25,True)
		if position == 3:
			GPIO.output(23,True)
			GPIO.output(24,True)
			GPIO.output(25,False)
		if position == 4:
			GPIO.output(23,False)
			GPIO.output(24,True)
			GPIO.output(25,False)
		if position == 5:
			GPIO.output(23,True)
			GPIO.output(24,False)
			GPIO.output(25,False)
		if position == 6:
			GPIO.output(23,False)
			GPIO.output(24,False)
			GPIO.output(25,False)
	if phase == 3:
		if position == 0:
			GPIO.output(17,True)
			GPIO.output(27,True)
			GPIO.output(22,True)
		if position == 1:
			GPIO.output(17,False)
			GPIO.output(27,True)
			GPIO.output(22,True)
		if position == 2:
			GPIO.output(17,True)
			GPIO.output(27,False)
			GPIO.output(22,True)
		if position == 3:
			GPIO.output(17,True)
			GPIO.output(27,True)
			GPIO.output(22,False)
		if position == 4:
			GPIO.output(17,False)
			GPIO.output(27,True)
			GPIO.output(22,False)
		if position == 5:
			GPIO.output(17,True)
			GPIO.output(27,False)
			GPIO.output(22,False)
		if position == 6:
			GPIO.output(17,False)
			GPIO.output(27,False)
			GPIO.output(22,False)





