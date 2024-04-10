import RPi.GPIO as GPIO
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 1, 1, 1, 1, 1, 1, 1]

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)


for i in range(8):
    GPIO.output(dac[i]*number[i],1)

time.sleep(10)

GPIO.output (dac, 0)

GPIO.cleanup()