import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

X=11
Y=15

GPIO.setup(X, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Y, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def stop():
    print("STOP!")
    GPIO.cleanup()

try:
    while True:
        input_stateA = GPIO.input(X)
        input_stateB = GPIO.input(Y)

        if input_stateA == False:
            print('Button Pressed')
            time.sleep(0.2)

        if input_stateB == False:
            print('Button Pressed')
            time.sleep(0.2)
except: KeyboardInterrupt:
    stop()
