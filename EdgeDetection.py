import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(23, GPIO.RISING)
    print ("Button 1 Pressed RISING")
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print ("Button 1 Pressed FALLING")

GPIO.cleanup()
