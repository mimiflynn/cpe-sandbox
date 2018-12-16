# Based on example code from:
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration

import time
from adafruit_circuitplayground.express import cpx
import simpleio

cpx.play_file("Wild Eep.wav")   # boot sound

print("Aloha")

cpx.pixels.brightness = 0.2

while True:
    if cpx.switch:
        print("Slide switch off!")
        cpx.pixels.fill((0, 0, 0))
        continue
    else:
        R = 0
        G = 0
        B = 0
        x, y, z = cpx.acceleration
        print((x, y, z))
        if x:
            R = R + abs(int(x))
        if y:
            G = G + abs(int(y))
        if z:
            B = B + abs(int(z))
        cpx.pixels.fill((R, G, B))

