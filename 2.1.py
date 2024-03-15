import RPi.GPIO as GPIO
from time import sleep


LED_PORTS = [2, 3, 4, 17, 27, 22, 10, 9]
SECONDS = 10
DELAY = 0.2

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PORTS, GPIO.OUT)

    GPIO.output(3, GPIO.LOW)
    sleep(1)

    GPIO.output(LED_PORTS, GPIO.LOW)

    cur_led = 0
    for _ in range(int(SECONDS / DELAY)):
        t = LED_PORTS[cur_led]
        GPIO.output(LED_PORTS[cur_led], GPIO.HIGH)
        sleep(DELAY)
        GPIO.output(LED_PORTS[cur_led], GPIO.LOW)
        cur_led = (cur_led + 1) % 8
    GPIO.cleanup()


main()
