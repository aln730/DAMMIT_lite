import sounddevice as sd
import numpy as np
import RPi.GPIO as GPIO

# GPIO pins
red = 11
green = 15
blue = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def set_color(r, g, b):
    GPIO.output(red, r)
    GPIO.output(green, g)
    GPIO.output(blue, b)

def audio_callback(indata, frames, time, status):
    volume = np.linalg.norm(indata)  # measure loudness

    if volume > 0.2:
        set_color(1, 0, 0)   # loud -> RED
    elif volume > 0.05:
        set_color(0, 1, 0)   # medium -> GREEN
    else:
        set_color(0, 0, 1)   # quiet -> BLUE

try:
    print("Listening...")
    with sd.InputStream(callback=audio_callback):
        while True:
            pass

except KeyboardInterrupt:
    pass

finally:
    set_color(0, 0, 0)
    GPIO.cleanup()
