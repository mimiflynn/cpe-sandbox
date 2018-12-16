# Based on example code from:
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration
# and
# https://learn.adafruit.com/combo-dial-safe-with-circuit-playground-express/code-with-circuitpython

import time
from adafruit_circuitplayground.express import cpx
import simpleio
print("Aloha")

cpx.pixels.brightness = 0.2
current_dial_position = 'X'

while True:
    if cpx.switch:
        print("Slide switch set to off!")
        cpx.pixels.fill((0, 0, 0))
        continue
    else:
        x, y, z = cpx.acceleration
        if x < 0 and y > 9:
            cpx.pixels[4] = (255, 0, 0)
            cpx.pixels[5] = (255, 0, 0)
            cpx.pixels[0] = (0, 0, 0)
            cpx.pixels[9] = (0, 0, 0)

        if x > 9 and y < 0:
            cpx.pixels[4] = (0, 0, 0)
            cpx.pixels[5] = (0, 0, 0)
            cpx.pixels[0] = (255, 0, 0)
            cpx.pixels[9] = (255, 0, 0)

        if x < 0 and y > -9:
            cpx.pixels[2] = (0, 0, 0)
            cpx.pixels[7] = (255, 0, 0)

        if x > -9 and y < 0:
            cpx.pixels[2] = (255, 0, 0)
            cpx.pixels[7] = (0, 0, 0)
