import RPi.GPIO as GPIO
import time

led = 18
period = 0.02
cycle=0.1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

#try:
while cycle < 0.0001: #fadein
    period =  period + 0.0001
    cycle = cycle - 0.001    
    GPIO.output(led, True)
    time.sleep(period * cycle)
    GPIO.output(led, False)
    time.sleep(period - (period * cycle))
    period =  period - 0.0001
    cycle = cycle + 0.005
while cycle > 0.01: #fadeout
    GPIO.output(led, True)
    time.sleep(period * cycle)
    GPIO.output(led, False)
    time.sleep(period - (period * cycle))
    period =  period + 0.0001
    cycle = cycle - 0.001
#except KeyboardInterrupt:
#    GPIO.cleanup()
    
