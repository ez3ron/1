from time import sleep
import RPi.GPIO as GPIO

# from button import *
# knopfsteuerung prototyp 0.1

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Verwendete Pins am Rapberry Pi
# Motor 1:
A=12   # in1
B=16   # in2
C=18   # in3
D=22   # in4

# Motor 2:
E=29    #in1
F=31    #in2
G=33    #in3
H=37    #in4

#################################
mo1 = 'A'
mo2 = 'B'

m1 = [A, B, C, D]
m2 = [E, F, G, H]

# zeit zwischen sequenzen
time = 0.0005

full = 512
halF = 256
vrtl = 128
ahtl = 64
zwtl = 32

# Pins aus Ausgange definieren
GPIO.setup(X, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Y, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)

GPIO.setup(E,GPIO.OUT)
GPIO.setup(F,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(H,GPIO.OUT)

GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)

GPIO.output(E, False)
GPIO.output(F, False)
GPIO.output(G, False)
GPIO.output(H, False)

# Schritte 1 - 8 festlegen
def Step1(m = m[]):
    GPIO.output(m[3], True)
    sleep (time)
    GPIO.output(m[3], False)

def Step2(m = []):
    GPIO.output(m[2], True)
    GPIO.output(m[3], True)
    sleep (time)
    GPIO.output(m[3], False)
    GPIO.output(m[2], False)

def Step3(m = []):
    GPIO.output(m[2], True)
    sleep(time)
    GPIO.output(m[2], False)

def Step4(m = []):
    GPIO.output(m[1], True)
    GPIO.output(m[2], True)
    sleep(time)
    GPIO.output(m[1], False)
    GPIO.output(m[2], False)

def Step5(m = []):
    GPIO.output(m[1], True)
    sleep(time)
    GPIO.output(m[1], False)

def Step6(m = []):
    GPIO.output(m[0], True)
    GPIO.output(m[1], True)
    sleep(time)
    GPIO.output(m[0], False)
    GPIO.output(m[1], False)

def Step7(m = []):
    GPIO.output(m[0], True)
    sleep(time)
    GPIO.output(m[0], False)

def Step8(m = []):
    GPIO.output(m[3], True)
    GPIO.output(m[0], True)
    sleep(time)
    GPIO.output(m[3], False)
    GPIO.output(m[0], False)

################################################
# Volle Umdrehung
def vorseq (m = []):
        Step1(m)
        Step2(m)
        Step3(m)
        Step4(m)
        Step5(m)
        Step6(m)
        Step7(m)
        Step8(m)

def rukseq (m = []):
        Step8(m)
        Step7(m)
        Step6(m)
        Step5(m)
        Step4(m)
        Step3(m)
        Step2(m)
        Step1(m)

################################################
# Vor / Rückdreuhung
def action_turn (lenge , motor, direc):
    for i in range (lenge):
        if (direc == 'vor'):
            print("VORWAERTS  <= !!")
            vorseq(m)
        elif (direc == 'ruk'):
            print("RUCKWAERTS <= !!")
            ruckseq(m)
    print (i)

##############################################
# stop & clear:
def stop():
    print("STOP!")
    GPIO.cleanup()

# Hauptprogramm:
try:
    action_turn(full, m1, 'vor')
    action_turn(full, m2, 'ruk')
    
except KeyboardInterrupt:
    stop()
finally:
    stop()
