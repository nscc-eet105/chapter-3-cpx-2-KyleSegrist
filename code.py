# Chapter 3 cpx lab-2
#CPX Back and forth LEDs

from adafruit_circuitplayground import cp
import time

BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
DELAY_TIME = .1

while True:

    for num in range(0,10):
        cp.pixels[num] = (RED)
        time.sleep(DELAY_TIME)
        cp.pixels[num] = (BLACK)
    for num in range(9,-1,-1):
        cp.pixels[num] = (BLUE)
        time.sleep(DELAY_TIME)
        cp.pixels[num] = (BLACK)
