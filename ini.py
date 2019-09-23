##Este código se ejecuta al iniciar la raspberry pi. Su finalidad es conectarse a 
##la base de datos, tomar los valores de resistencia en cada fase y activar
##los gpio correspondientes
#Libraries
import functions as fu

#Database connection
c,phase1,phase2,phase3=fu.conx_ret()

#Phase1
if phase1 == "0":
	fu.send_gpio(1,0)
elif phase1 == "1":
        fu.send_gpio(1,1)
elif phase1 == "2":
        fu.send_gpio(1,2)
elif phase1 == "3":
        fu.send_gpio(1,3)
elif phase1 == "4":
        fu.send_gpio(1,4)
elif phase1 == "5":
        fu.send_gpio(1,5)
elif phase1 == "6":
        fu.send_gpio(1,6)
#phase2
if phase2 == "0":
    fu.send_gpio(2,0)
elif phase2 == "1":
        fu.send_gpio(2,1)
elif phase2 == "2":
        fu.send_gpio(2,2)
elif phase2 == "3":
        fu.send_gpio(2,3)
elif phase2 == "4":
        fu.send_gpio(2,4)
elif phase2 == "5":
        fu.send_gpio(2,5)
elif phase2 == "6":
        fu.send_gpio(2,6)
#phase3
if phase3 == "0":
    fu.send_gpio(3,0)
elif phase3 == "1":
        fu.send_gpio(3,1)
elif phase3 == "2":
        fu.send_gpio(3,2)
elif phase3 == "3":
        fu.send_gpio(3,3)
elif phase3 == "4":
        fu.send_gpio(3,4)
elif phase3 == "5":
        fu.send_gpio(3,5)
elif phase3 == "6":
        fu.send_gpio(3,6)
