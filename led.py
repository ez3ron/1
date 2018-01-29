import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setwarnings(False)


while 1:

    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(7, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(7, GPIO.LOW)



