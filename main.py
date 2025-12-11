import RPi.GPIO as GPIO
import time
import math
import random

# --- GPIO pins ---
RED = 11
GREEN = 15
BLUE = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

# --- PWM for smooth brightness ---
red_pwm = GPIO.PWM(RED, 1000)
green_pwm = GPIO.PWM(GREEN, 1000)
blue_pwm = GPIO.PWM(BLUE, 1000)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

def set_color(r, g, b):
    """Set RGB LED color (0-100%)"""
    red_pwm.ChangeDutyCycle(r)
    green_pwm.ChangeDutyCycle(g)
    blue_pwm.ChangeDutyCycle(b)

# --- Pattern 1: Smooth rainbow fade ---
def rainbow_fade(duration=5, steps=100):
    for i in range(steps):
        t = i / steps
        r = (math.sin(t * math.pi * 2) + 1) / 2 * 100
        g = (math.sin(t * math.pi * 2 + 2) + 1) / 2 * 100
        b = (math.sin(t * math.pi * 2 + 4) + 1) / 2 * 100
        set_color(r, g, b)
        time.sleep(duration / steps)

# --- Pattern 2: Random flashes ---
def random_flash(times=20):
    for _ in range(times):
        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        set_color(r, g, b)
        time.sleep(0.2)

# --- Pattern 3: Breathing effect ---
def breathing(duration=5, steps=50):
    for i in range(steps):
        t = (math.sin(math.pi * i / steps) + 1) / 2 * 100
        set_color(t, t/2, 100-t)
        time.sleep(duration / steps)

# --- Main loop ---
try:
    while True:
        rainbow_fade()
        random_flash()
        breathing()

except KeyboardInterrupt:
    pass

finally:
    set_color(0, 0, 0)
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
