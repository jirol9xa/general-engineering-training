import RPi.GPIO as GPIO
import itertools

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(14, GPIO.IN)

for i in itertools.count(0, step = 1):
    print(17, GPIO.input(14))