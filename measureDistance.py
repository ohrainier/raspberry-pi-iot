import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print "Distance measurement in progress"
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(TRIG, False)
        print "Waiting for sensor to settle"

        time.sleep(0.5)

        print "sleep 2"

        GPIO.output(TRIG, True)
        time.sleep(0.00001)

        print "time.sleep(0.00001)"
        
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
            print "echo 0", GPIO.input(ECHO), start
            
        while GPIO.input(ECHO) == 1:
            stop = time.time()
            print "echo 1", stop, start

            
        elapsed = stop - start

        distance = elapsed * 17000

        distance = round (distance, 2)

        if distance > 2 and distance < 400:
            print "Distance: %.1f" % distance
        else:
            print "Distance out of rance"

except KeyboardInterrupt:
    print "User Interrupt"
    GPIO.cleanup()
