import mysql.connector
import RPi.GPIO as GPIO
import time
import functions as fu
import smbus

## GPIO inicialización
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
## enable using mcp23017 with i2c protocol
bus = smbus.SMBus(1)
##Set chip address, and enable GPIOA as outputs
bus.write_byte_data(0x20,0x00,0x00)
## Conexión con la base de datos para consultar el valor de control
control,p1,p2,p3 = fu.conx_ret()
cont_con = int(control)
## Loop del código principal
while True:
	if cont_con == 1:
		bus.write_byte_data(0x20,0x14,0x01)
	if cont_con == 0:
		bus.write_byte_data(0x20,0x14,0x00)
	##Conexión nuevamente a la base de datos para enviar el valor de botón
	##de control
	con = mysql.connector.connect(host = 'localhost',user = 'jose5',password = '12345', database = 'database', autocommit = True)
	cursor = con.cursor()
	control = GPIO.input(7)
	if control == False:
		cont_con = cont_con + 1
		time.sleep(0.2)
		if cont_con > 1:
			cont_con = 0
	cursor.execute("UPDATE info2 SET control ="+str(cont_con))
	print(cont_con)
	cursor.close()
	con.close()
