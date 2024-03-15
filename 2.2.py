import RPi.GPIO as GPIO


DAC = [8, 11, 7, 1, 0, 5, 12, 6]

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DAC, GPIO.OUT)
    GPIO.output(DAC, GPIO.LOW)

    for n in [255, 127, 64, 32, 5, 0, 256]:
        s = bin(n)[2:]
        s = '0' * (8 - len(s)) + s
        GPIO.output(DAC, list(map(int, s)))
        input()

    GPIO.output(DAC, [0] * 8)
    GPIO.cleanup()


main()
