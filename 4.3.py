import RPi.GPIO as GPIO
from time import sleep

P = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def main():
    GPIO.setup(P, GPIO.OUT)

    p = GPIO.PWM(P, 1000)
    p.start(0)

    try:
        while True:
            s = input("Set duty cycle: ")
            if s == 'q': break

            try:
                s = float(s)
                p.ChangeDutyCycle(s)
                print(3.3 * s / 100)
            except ValueError:
                print("Input an integer")
            
    finally:
        p.stop()
        GPIO.output(P, 0)
        GPIO.cleanup()
            
if __name__ == '__main__':
    main()
