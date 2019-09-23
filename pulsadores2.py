#libraries
import time
import functions as fu
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi,noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text,show_message
from luma.core.legacy.font import proportional, TINY_FONT

#Variable initialization
cont_phase = 0
cont_pos = 0
serial = spi(port = 0, device = 0, gpio = noop())
device = max7219(serial, cascaded = 1, block_orientation = 0, rotate = 0)

#Function to use led matrix
def led_matrix(msj):
	with canvas(device) as draw:
		text(draw,(0,1),msj, fill = "white", font = proportional(TINY_FONT))
		device.contrast(20)
#Main loop
while True:
	#Database connection
	control,p1,p2,p3= fu.conx_ret()
	#If manual control is enabled, then discriminate phases and positions
	if control == "1":
		phase,position_pos = fu.pul()
		#Buttons control
		if phase == False:
			cont_phase = cont_phase + 1
			cont_pos = 0
			time.sleep(0.2)
			if cont_phase > 3:
				cont_phase = 1
		if position_pos == False:
			cont_pos = cont_pos + 1
			time.sleep(0.2)
			if cont_pos > 6:
				cont_pos = 0
		if cont_phase == 0:
			if cont_pos == 0:
				led_matrix("on")
		#Phase and position discrimation
		if cont_phase == 1:
			if cont_pos == 0:
				fu.conx_send(1,0)
				fu.send_gpio(1,0)
				led_matrix("10")
			if cont_pos == 1:
				fu.conx_send(1,1)
				fu.send_gpio(1,1)
				led_matrix("11")
			if cont_pos == 2:
				fu.conx_send(1,2)
				fu.send_gpio(1,2)
				led_matrix("12")
			if cont_pos == 3:
				fu.conx_send(1,3)
				fu.send_gpio(1,3)
				led_matrix("13")
			if cont_pos == 4:
				fu.conx_send(1,4)
				fu.send_gpio(1,4)
				led_matrix("14")
			if cont_pos == 5:
				fu.conx_send(1,5)
				fu.send_gpio(1,5)
				led_matrix("15")
			if cont_pos == 6:
				fu.conx_send(1,6)
				fu.send_gpio(1,6)
				led_matrix("16")
		if cont_phase == 2:
			if cont_pos == 0:
				fu.conx_send(2,0)
				fu.send_gpio(2,0)
				led_matrix("20")
			if cont_pos == 1:
				fu.conx_send(2,1)
				fu.send_gpio(2,1)
				led_matrix("21")
			if cont_pos == 2:
				fu.conx_send(2,2)
				fu.send_gpio(2,2)
				led_matrix("22")
			if cont_pos == 3:
				fu.conx_send(2,3)
				fu.send_gpio(2,3)
				led_matrix("23")
			if cont_pos == 4:
				fu.conx_send(2,4)
				fu.send_gpio(2,4)
				led_matrix("24")
			if cont_pos == 5:
				fu.conx_send(2,5)
				fu.send_gpio(2,5)
				led_matrix("25")
			if cont_pos == 6:
				fu.conx_send(2,6)
				fu.send_gpio(2,6)
				led_matrix("26")
		if cont_phase == 3:
			if cont_pos == 0:
				fu.conx_send(3,0)
				fu.send_gpio(3,0)
				led_matrix("30")
			if cont_pos == 1:
				fu.conx_send(3,1)
				fu.send_gpio(3,1)
				led_matrix("31")
			if cont_pos == 2:
				fu.conx_send(3,2)
				fu.send_gpio(3,2)
				led_matrix("32")
			if cont_pos == 3:
				fu.conx_send(3,3)
				fu.send_gpio(3,3)
				led_matrix("33")
			if cont_pos == 4:
				fu.conx_send(3,4)
				fu.send_gpio(3,4)
				led_matrix("34")
			if cont_pos == 5:
				fu.conx_send(3,5)
				fu.send_gpio(3,5)
				led_matrix("35")
			if cont_pos == 6:
				fu.conx_send(3,6)
				fu.send_gpio(3,6)
				led_matrix("36")
	else:
		led_matrix("--")


