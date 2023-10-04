# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import task1 as am
import time

fig, ax = plt.subplots()


class CelestialBody():
    def __init__(self,
                 pos=np.array([0, 0]),
                 surrounds=None,
                 surround_velocity=0,
                 own_velocity=0,
                 color='.',
                 ):

        self.surrounds = surrounds
        self.pos = pos
        self.surround_velocity = surround_velocity
        self.own_velocity = own_velocity
        self.line, = plt.plot([], [], color)

    def update(self, frame):

        if self.surrounds:
            if self.surrounds.surrounds:
                self.pos = am.rotate_around_point(self.pos, *self.surrounds.surrounds.pos,
                                                  self.surrounds.surround_velocity)
            self.pos = am.rotate_around_point(self.pos, *self.surrounds.pos, self.surround_velocity)
        e = am.rectangle(*self.pos, 0.4, 0.4, self.own_velocity * frame)
        self.line.set_data(e)


n_per_day = 7
n_days = 365
n = n_days * n_per_day  # number of iterations

sun = CelestialBody(pos=np.array([0, 0]), own_velocity=2, color='y')
earth = CelestialBody(pos=np.array([-3, 0]), surrounds=sun, surround_velocity=2 * np.pi / n,
                      own_velocity=2 * np.pi / (n / 365), color='b')
moon = CelestialBody(pos=np.array([-3, 1]), surrounds=earth, surround_velocity=2. * np.pi / (n / 12.),
                     own_velocity=2. * np.pi / (n / 12.), color='black')
t = plt.text(*sun.pos + np.array([-1, -1]), "")


def init():
    ax.axis([-5, 5, -5, 5])
    ax.set_aspect('equal', 'box')


def update(frame):
    moon.update(frame)
    sun.update(frame)
    earth.update(frame)
    s = f"h: {frame % 24:0>2} days: {(frame / 24) % 28:1.2f} months: {(frame / 24) / 28:1.2f}"
    t.set_text(s)


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
plt.show()