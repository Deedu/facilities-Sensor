import RPi.GPIO as GPIO


CHANNEL =10

GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL,GPIO.IN)

print(GPIO.input(CHANNEL))