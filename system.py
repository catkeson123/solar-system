# Author: Calvin Atkeson
# Date: 10/23/21
# Purpose: Lab 2 System class

from body import Body
from math import sqrt

# gravitational constant
G = 6.67384e-11

class System:
    # initial function of the class
    # takes in a list of bodies
    def __init__(self, body_list):
        self.body_list = body_list

    # updates the system
    # takes in the timestep
    def update(self, timestep):
        for body in self.body_list:
            body.update_position(timestep)
        for body in self.body_list:
            (ax, ay) = self.compute_acceleration(body)
            body.update_velocity(ax, ay, timestep)

    # draws the system
    # takes in the center of the window and the scale of simulation
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)

    # computes the acceleration of a body
    # takes in the index n of the body
    def compute_acceleration(self, n):
        ax = 0
        ay = 0

        for body in self.body_list:
            if body is not n:
                # x and y distances from each body and total distance
                dx = n.x - body.x
                dy = n.y - body.y
                r = sqrt((dx * dx) + (dy * dy))
                # total acceleration and x and y accelerations
                a = (G * body.mass) / (r * r)
                ax1 = a * dx / r
                ay1 = a * dy / r
                # add to total acceleration
                ax = ax + ax1
                ay = ay + ay1
        return (ax, ay)
