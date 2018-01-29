import RPi.GPIO as GPIO
from time import sleep

#inervalllänge:
# 02.01.2018
# Motor dreht Vorwärts dan Rückwerts, DC motor
# pin 23, pin 24, pin 25


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

Motor1 = 16
Motor2 = 18
Motor3 = 22

GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2, GPIO.OUT)
GPIO.setup(Motor3, GPIO.OUT)

def vorwärts (n):
    print("Forwärts!")

    GPIO.output(Motor1, GPIO.LOW)
    GPIO.output(Motor2, GPIO.HIGH)
    GPIO.output(Motor3, GPIO.HIGH)

    for i in range(0, n):
        sleep(1)
        print (i)

def rückwerts (n):
    print("Rückwärts!")

    GPIO.output(Motor1, GPIO.HIGH)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.HIGH)

    for i in range(0, n):
        sleep(1)
        print (i)
    
def stop ():
    print("STOP!")

    GPIO.output(Motor3, GPIO.LOW)

    #aufräumen!
    GPIO.cleanup()
    

vorwärts(10)
rückwerts(5)
stop()
