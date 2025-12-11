import RPi.GPIO as GPIO
import time
import random

# --- GPIO pins ---
RED = 11
GREEN = 15
BLUE = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

def set_color(r, g, b):
    """Set RGB color (1 = on, 0 = off)"""
    GPIO.output(RED, r)
    GPIO.output(GREEN, g)
    GPIO.output(BLUE, b)

# --- Pattern 1: Random flashes ---
def random_flash(times=20):
    for _ in range(times):
        r = random.randint(0, 1)
        g = random.randint(0, 1)
        b = random.randint(0, 1)
        set_color(r, g, b)
        time.sleep(0.2)

# --- Pattern 2: RGB chase ---
def rgb_chase(times=10, speed=0.3):
    for _ in range(times):
        set_color(1,0,0)
        time.sleep(speed)
        set_color(0,1,0)
        time.sleep(speed)
        set_color(0,0,1)
        time.sleep(speed)

# --- Pattern 3: All on/off strobe ---
def strobe(times=10, speed=0.1):
    for _ in range(times):
        set_color(1,1,1)
        time.sleep(speed)
        set_color(0,0,0)
        time.sleep(speed)

# --- Main loop ---
try:
    while True:
        random_flash()
        rgb_chase()
        strobe()

except KeyboardInterrupt:
    pass

finally:
    set_color(0,0,0)
    GPIO.cleanup()
