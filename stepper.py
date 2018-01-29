
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

# Verwendete Pins am Rapberry Pi
A=12   # in1
B=16   # in2
C=18   # in3
D=22   # in4


E=29
F=31
G=33
H=37


X=15   # Button
Y=11
time = 0.0009


full = 512
halF = 256
vrtl = 128
ahtl = 64
zwtl = 32


# Pins aus Ausgange definieren
GPIO.setup(X, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)

GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)

# Schritte 1 - 8 festlegen
def Step1():
    GPIO.output(D, True)
    sleep (time)
    GPIO.output(D, False)

def Step1B():
    GPIO.output(H, True)
    sleep (time)
    GPIO.output(H, False)


def Step2():
    GPIO.output(C, True)
    GPIO.output(D, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(C, False)

def Step2B():
    GPIO.output(G, True)
    GPIO.output(H, True)
    sleep (time)
    GPIO.output(H, False)
    GPIO.output(G, False)

def Step3():
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(C, False)

def Step3B():
    GPIO.output(G, True)
    sleep (time)
    GPIO.output(G, False)

def Step4():
    GPIO.output(B, True)
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(B, False)
    GPIO.output(C, False)

def Step4B():
    GPIO.output(F, True)
    GPIO.output(G, True)
    sleep (time)
    GPIO.output(F, False)
    GPIO.output(G, False)

def Step5():
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(B, False)

def Step5B():
    GPIO.output(F, True)
    sleep (time)
    GPIO.output(F, False)

def Step6():
    GPIO.output(A, True)
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(A, False)
    GPIO.output(B, False)

def Step6B():
    GPIO.output(E, True)
    GPIO.output(F, True)
    sleep (time)
    GPIO.output(E, False)
    GPIO.output(F, False)

def Step7():
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(A, False)

def Step8():
    GPIO.output(D, True)
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(A, False)

# Volle Umdrehung
def sequee1 ():
        Step1()
        Step2()
        Step3()
        Step4()
        Step5()
        Step6()
        Step7()
        Step8()

def sequee2 ():
        Step8()
        Step7()
        Step6()
        Step5()
        Step4()
        Step3()
        Step2()
        Step1()

def volldrehung (art):
    print("vorwarts!")
    for i in range (art):    
        sequee1()
#	if (i % 15) == 0 :  
        print (i)

def ruckdrehung (art):
    print("ruckwarts!")
    for i in range (art):    
        sequee2()  
#	if (i % 15) == 0 :
        print (i)

def stop():
    print("STOP!")
    GPIO.cleanup()

try:
	while True:
		
		if GPIO.input(15):
			volldrehung(full)
			ruckdrehung(full)
			volldrehung(vrtl)
			ruckdrehung(vrtl)
			volldrehung(zwtl)
		else: 
			print("DRUEKE KNOPF!")

		sleep(0.1)
	
except KeyboardInterrupt:
	stop()

finally:
	stop()
