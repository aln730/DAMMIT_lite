import sounddevice as sd
import numpy as np
import RPi.GPIO as GPIO
import time
import random

RED = 11
GREEN = 15
BLUE = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

pwm_r = GPIO.PWM(RED, 500)
pwm_g = GPIO.PWM(GREEN, 500)
pwm_b = GPIO.PWM(BLUE, 500)

pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

def set_color(r, g, b):
    pwm_r.ChangeDutyCycle(r)
    pwm_g.ChangeDutyCycle(g)
    pwm_b.ChangeDutyCycle(b)

SAMPLE_RATE = 44100
CHUNK = 1024

def callback(indata, frames, time_info, status):
    audio = np.mean(indata, axis=1)
    fft = np.abs(np.fft.rfft(audio))

    bass  = np.mean(fft[0:80])     
    mids  = np.mean(fft[80:300])    
    highs = np.mean(fft[300:800])    

    scale = 0.0005

    # Create a list of the three frequency values
    freqs = [bass, mids, highs]
    random.shuffle(freqs)  # shuffle them

    # Map the shuffled values to RGB randomly
    r = min(freqs[0] * scale, 1) * 100
    g = min(freqs[1] * scale, 1) * 100
    b = min(freqs[2] * scale, 1) * 100

    set_color(r, g, b)

print("🎤 Mic visualizer running… Ctrl+C to stop.")

try:
    with sd.InputStream(callback=callback,
                        channels=2,
                        samplerate=SAMPLE_RATE,
                        blocksize=CHUNK):
        while True:
            time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    set_color(0, 0, 0)
    GPIO.cleanup()
    print("LEDs off. Goodbye!")
