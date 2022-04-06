import RPi.GPIO as GPIO
import itertools
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for i in itertools.count(0, step = 1):
    GPIO.output(17, i % 2)
    time.sleep(1.0)