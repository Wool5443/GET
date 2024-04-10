import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
GPIO.setup (26, GPIO.OUT)
GPIO.setup (16, GPIO.IN)
input()
GPIO.output (26, GPIO.input (16))