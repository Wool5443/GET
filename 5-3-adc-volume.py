import RPi.GPIO as GPIO
from time import sleep

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

def to_bin(n):
    s = bin(n)[2:].zfill(8)
    return list(map(int, s))

def adc1():
    for i in range(256):
        dac_val = to_bin(i)
        GPIO.output(dac, dac_val)
        comp_val = GPIO.input(comp)
        sleep(0.01)
        if comp_val:
            return i
    return 0

def adc2():
    k = 0
    for i in range(7, -1, -1):
        k += 2 ** i
        dac_val = to_bin(k)
        GPIO.output(dac, dac_val)
        sleep(0.01)
        cmp = GPIO.input(comp)
        if cmp == GPIO.HIGH:
            k -= 2 ** i
    return k

def Volume(val):
    val = int(val / 256 * 10)
    arr = [0] * 8
    for i in range(val - 1):
        arr[i] = 1
    return arr

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(leds, GPIO.OUT)
    GPIO.setup(dac, GPIO.OUT)
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(comp, GPIO.IN)

    try:
        while True:
            i = adc2()
            voltage = i * 3.3 / 256.0
            if i: print(f"{voltage:.2f}")
            arr = Volume(i)
            GPIO.output(leds, arr)
    finally:
        GPIO.output(dac, 0)
        GPIO.cleanup()

if __name__ == '__main__':
    main()
