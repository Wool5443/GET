import RPi.GPIO as GPIO


LEDS = [2, 3, 4, 17, 27, 22, 10, 9]
AUX = [21, 20, 26, 16, 19, 25, 23, 24]

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDS, GPIO.OUT)
    GPIO.setup(AUX, GPIO.IN)

    GPIO.output(LEDS, GPIO.LOW)

    while True:
        for i in range(len(LEDS)):
            GPIO.output(LEDS[i], GPIO.input(AUX[i]))


main()
