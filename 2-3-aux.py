import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7,  8,  25, 24]
aux  = [22, 23, 27, 18, 15, 14, 3,  2]

[GPIO.setup(leds[i], GPIO.OUT) for i in range(8)]
[GPIO.setup(aux[i],  GPIO.IN)  for i in range(8)]

while 1:
    [GPIO.output(leds[i], GPIO.input(aux[i])) for i in range(8)]
    time.sleep(1.0)

[GPIO.output(leds[k], 0) for k in range(8)]
GPIO.cleanup()