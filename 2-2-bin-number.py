import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac     = [26, 19, 13, 6, 5, 11, 9, 10]
number  = [0, 1, 1, 1, 1, 1, 1, 1]

[GPIO.setup(dac[i], GPIO.OUT) for i in range(8)]

[GPIO.output(dac[i], number[i]) for i in range(8)]

time.sleep(20.0)

[GPIO.output(dac[k], 0) for k in range(8)]
GPIO.cleanup()
    
