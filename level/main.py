# Based on example code from:
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration
# and
# https://learn.adafruit.com/combo-dial-safe-with-circuit-playground-express/code-with-circuitpython

import time
from adafruit_circuitplayground.express import cpx
# https://circuitpython.readthedocs.io/projects/simpleio/en/latest/
import simpleio
print("Aloha")

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.05

while True:
    if cpx.switch:
        print("Slide switch set to off!")
        cpx.pixels.fill((0, 0, 0))
        continue
    else:
        x, y, z = cpx.acceleration

        x_value = abs(int(simpleio.map_range(x, -10, 10, 0, 10)))
        y_value = abs(int(simpleio.map_range(y, -10, 10, 0, 10)))
        z_value = abs(int(simpleio.map_range(z, -10, 10, 0, 10)))

        print((x_value, y_value, z_value))

        if x_value >= 9:
            cpx.pixels[2] = (0, 150, 150)
        else:
            cpx.pixels[2] = (0, 0, 0)

        if x_value >= 7 and y_value >= 3:
            cpx.pixels[3] = (0, 150, 150)
        else:
            cpx.pixels[3] = (0, 0, 0)

        if x_value >= 7 and y_value <= 3:
            cpx.pixels[1] = (0, 150, 150)
        else:
            cpx.pixels[1] = (0, 0, 0)

        if x_value <= 3 and y_value >= 3:
            cpx.pixels[6] = (0, 150, 150)
        else:
            cpx.pixels[6] = (0, 0, 0)

        if x_value <= 3 and y_value <= 7:
            cpx.pixels[8] = (0, 150, 150)
        else:
            cpx.pixels[8] = (0, 0, 0)

        if x_value <= 1:
            cpx.pixels[7] = (0, 150, 150)
        else:
            cpx.pixels[7] = (0, 0, 0)

        if y_value >= 9:
            cpx.pixels[4] = (0, 150, 150)
            cpx.pixels[5] = (0, 150, 150)
        else:
            cpx.pixels[4] = (0, 0, 0)
            cpx.pixels[5] = (0, 0, 0)

        if y_value <= 1:
            cpx.pixels[0] = (0, 150, 150)
            cpx.pixels[9] = (0, 150, 150)
        else:
            cpx.pixels[0] = (0, 0, 0)
            cpx.pixels[9] = (0, 0, 0)

    cpx.pixels.show()
    time.sleep(0.05)
