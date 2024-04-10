import RPi.GPIO as GPIO
from time import sleep

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

def to_bin(n):
    s = bin(n)[2:].zfill(8)
    return list(map(int, s))

def adc():
    for i in range(256):
        dac_val = to_bin(i)
        GPIO.output(dac, dac_val)
        comp_val = GPIO.input(comp)
        sleep(0.01)
        if comp_val:
            return i
    return 0

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT)
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(comp, GPIO.IN)

    try:
        while True:
            i = adc()
            voltage = i * 3.3 / 256.0
            if i: print(f"{voltage:.2f}")
    finally:
        GPIO.output(dac, 0)
        GPIO.cleanup()

if __name__ == '__main__':
    main()
