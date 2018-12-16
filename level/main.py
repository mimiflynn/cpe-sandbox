# Based on example code from:
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration
# and
# https://learn.adafruit.com/combo-dial-safe-with-circuit-playground-express/code-with-circuitpython


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





import time
from adafruit_circuitplayground.express import cpx
import simpleio

cpx.play_file("Wild Eep.wav")   # Play a coin sound on boot

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
        print((x, y, z))
        if x == 0 and y == 9:
            current_dial_position = 'A'  # used to store dial position
            cpx.pixels[0] = (255, 0, 0)
            cpx.pixels[9] = (255, 0, 0)

        if x == 9 and y == 0:
            current_dial_position = 'B'
            cpx.pixels[4] = (255, 0, 0)
            cpx.pixels[5] = (255, 0, 0)

        if x == 0 and y == -9:
            current_dial_position = 'C'
            cpx.pixels[2] = (255, 0, 0)

        if x == -9 and y == 0:
            current_dial_position = 'D'
            cpx.pixels[7] = (255, 0, 0)

        print(current_dial_position)

