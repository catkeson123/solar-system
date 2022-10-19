# Author: Calvin Atkeson
# Date 10/27/21
# Purpose: Solar system driver

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3e6     # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

sun = Body(1.998892e30, 0, 0, 0, 0, 15, 1, .7, .2)
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 3, .5, .5, .5)
venus = Body(4.87e24, -108.2e9, 0, 0 , 35040, 6, 0, 1, 0)
earth = Body(5.9736e24, -149.6e9, 0, 0, 29790, 7, 0, 0, 1)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 4, 1, 0, 0)

solar_system = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)
