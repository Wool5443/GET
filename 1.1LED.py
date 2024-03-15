import RPi.GPIO as GPIO


IN_PORT    = 24
OUT_PORT   = 26

def main():
    GPIO.cleanup()
    return
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUT_PORT, GPIO.OUT)
    GPIO.setup(IN_PORT,  GPIO.IN)

    while True:
        GPIO.output(OUT_PORT, GPIO.input(IN_PORT))
        input()


main()
