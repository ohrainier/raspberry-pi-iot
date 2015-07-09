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

def fadeMain():
    fadeOut(cycle,period,incrementer)
    cycle = 0.005
    period = 0.02
    incrementer = .002
    fadeIn(cycle,period,incrementer)
    period = 0.02
    cycle = 1
    incrementer = .005

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

period = 0.02
cycle = 1
incrementer = .005

try:
    process = True
    while(process):
        led = 15
        GPIO.setup(led, GPIO.OUT)
        fadeMain(cycle,period,incrementer)
        led = 16
        GPIO.setup(led, GPIO.OUT)
        fadeMain(cycle,period,incrementer)
        led = 18
        GPIO.setup(led, GPIO.OUT)
        fadeMain(cycle,period,incrementer) 

                
except KeyboardInterrupt:
    process = False
    GPIO.cleanup()
