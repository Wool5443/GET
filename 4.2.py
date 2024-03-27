import RPi.GPIO as GPIO
from time import sleep


DAC = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def getBin(n):
    s = bin(n)[2:]
    return list(map(int, '0' * (8 - len(s)) + s))

def main():
    GPIO.setup(DAC, GPIO.OUT)

    x = 0
    dx = 1

    period = 0.0
    s = input("Set signal period in s: ")

    try:
        period = float(s)
    except ValueError:
        print("Input not a number!!!")

    sleepTime = period / 512

    try:
        while (True):
            if x == 0:
                dx = 1
            elif x == 255:
                dx = -1
            
            GPIO.output(DAC, getBin(x))
            x += dx

            print(f"Current voltage = {x * 3.3 / 256.0:.4f}")
            sleep(sleepTime)

    finally:
        GPIO.output(DAC, [0] * len(DAC))
        
        


if __name__ == '__main__':
    main()
