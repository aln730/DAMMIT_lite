import soundfile as sf
import numpy as np
import RPi.GPIO as GPIO
import time

# --- GPIO pins ---
RED = 11
GREEN = 15
BLUE = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

def set_color(r, g, b):
    GPIO.output(RED, r)
    GPIO.output(GREEN, g)
    GPIO.output(BLUE, b)

# Load audio file
filename = "song.wav"  # your WAV file
data, samplerate = sf.read(filename)

# Normalize if stereo
if len(data.shape) > 1:
    data = data.mean(axis=1)

# Process audio in small chunks
chunk_size = 1024
num_chunks = len(data) // chunk_size

try:
    for i in range(num_chunks):
        chunk = data[i*chunk_size:(i+1)*chunk_size]
        volume = np.linalg.norm(chunk)

        if volume > 0.5:
            set_color(1, 0, 0)  # Loud → RED
        elif volume > 0.2:
            set_color(0, 1, 0)  # Medium → GREEN
        else:
            set_color(0, 0, 1)  # Quiet → BLUE

        time.sleep(chunk_size / samplerate)  # real-time pacing

except KeyboardInterrupt:
    pass
finally:
    set_color(0,0,0)
    GPIO.cleanup()
