def fadeOut(cycle,period,incrementer):
    for i in range(1, 100):
        while True:
            if(period * cycle < 0):
                break
            GPIO.output(led, True)
            time.sleep(period * cycle)
            GPIO.output(led, False)
            time.sleep(period-(period*cycle))
            cycle = cycle - incrementer

def fadeIn(cycle,period,incrementer):
    for i in range(1, 100):
        while True:
            #fadein
            cycle = cycle + incrementer
            time.sleep(period+(period*cycle))
            GPIO.output(led, True)
            time.sleep(period * cycle)
            GPIO.output(led, False)                
            if(period * cycle > 0):
                break 

import RPi.GPIO as GPIO
import time

led = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    GPIO.wait_for_edge(16, GPIO.RISING)
    period = 0.02
    cycle = 1
    incrementer = .005
    fadeOut(cycle,period,incrementer)
    cycle = 0.005
    period = 0.005
    incrementer = .005
    fadeIn(cycle,period,incrementer)


GPIO.cleanup()
