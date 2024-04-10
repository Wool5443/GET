import RPi.GPIO as GPIO

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setmode (GPIO.BCM)
GPIO.setup (aux, GPIO.IN)
GPIO.setup (leds, GPIO.OUT)

GPIO.output(leds, 1)

while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))

GPIO.output(leds, 0)

GPIO.cleanup()