# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import augmentedmethods as am

ce =      [0.0,5.0]                             # start coordinates of earth
sun =      [0.0,0.0]                              # coordinates of the sun

n_per_day =  1
n_days =  365
n = n_days*n_per_day                            # number of iterations
phi_rotate =  2*np.pi / n_days / n_per_day      # angular velocity earth - sun
earth_rotate = 1

ce = np.append(ce,1)

ce_list = [ce]
for i in range(n):
    ce = am.rotate_around_point(ce,sun[0],sun[1],phi_rotate)
    ce_list.append(ce)
           # generate coordinates

# Initialize the figure and axis
fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
center_dot, = plt.plot([], [], '.r')


def init():
    ax.axis([-10,10,-10,10])
    ax.set_aspect('equal', 'box')
  
    return center_dot,


def update(frame):
    ce_frame = ce_list[frame]
    center_dot.set_data(ce_frame[0],ce_frame[1])
   
    
    return center_dot, 


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
fig.show()
plt.show()
