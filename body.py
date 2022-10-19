# Author: Calvin Atkeson
# Date: 10/23/21
# Purpose: Lab 2 Body class

from cs1lib import *

class Body:
    # initial function of the class
    # takes in the physical properties and color of body
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    # updates the position of the body
    # takes in the timestep
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    # updates the velocity of the body
    # takes in the acceleration and the timestep
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx - ax * timestep
        self.vy = self.vy - ay * timestep

    # draws each body
    # takes in the center of the window and the scale of simulation
    def draw(self, cx, cy, pixels_per_meter):
        # new position for body
        new_x = cx + self.x * pixels_per_meter
        new_y = cy + self.y * pixels_per_meter

        # draw the body
        set_fill_color(self.r, self.g, self.b)
        draw_circle(new_x, new_y, self.pixel_radius)
