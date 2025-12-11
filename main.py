import time
import RPi.GPIO as GPIO

# RGB pins (BOARD numbering)
redPin = 11
greenPin = 15
bluePin = 13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

def all_off():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)

try:
    print("Testing RED...")
    GPIO.output(redPin, GPIO.HIGH)
    time.sleep(1)
    all_off()

    print("Testing GREEN...")
    GPIO.output(greenPin, GPIO.HIGH)
    time.sleep(1)
    all_off()

    print("Testing BLUE...")
    GPIO.output(bluePin, GPIO.HIGH)
    time.sleep(1)
    all_off()

    print("Done.")

finally:
    all_off()
    GPIO.cleanup()
