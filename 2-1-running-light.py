import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

[GPIO.setup(leds[i], GPIO.OUT) for i in range(8)]

for j in range(3):

    for i in range(0, 8):
        [GPIO.output(leds[k], 0) for k in range(8)]
        GPIO.output(leds[i], 1)
        time.sleep(0.2)

[GPIO.output(leds[k], 0) for k in range(8)]
GPIO.cleanup()
    