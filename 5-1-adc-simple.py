import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
troyka = 17
cmp = 4
levels = 2**bits
maxvoltage = 3.3

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(cmp, GPIO.IN)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

i = 0

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal


try:
    while True:
        for value in range(256):
            signal = num2dac(value)
            voltage = value / levels * maxvoltage
            time.sleep(0.0001)
            comparatorValue = GPIO.input(cmp)
            if comparatorValue == 0:
                print("ADC value = {:^3} -> {}, input voltage = {:2f}".format(value, signal, voltage))
                break
except KeyboardInterrupt:
    print("\nThe program was stopped by the keyboard")
else:
    print("No exeptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")