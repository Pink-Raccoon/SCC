# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import augmentedmethods as am

# Initialize the coordinates of the Earth and the Sun
ce = np.array([5.0, 0.0])  # Start coordinates of Earth
sun = np.array([0, 0, 1])       # Coordinates of the Sun

# Parameters for the animation
n_per_day = 1
n_days = 365
n = n_days * n_per_day          # Number of iterations
phi_rotate = 2 * np.pi / n_days / n_per_day  # Angular velocity earth - sun

# Side length of the square representing Earth
side_len = 1.0
hori = np.array([side_len/2,0])
verti = np.array([0,side_len/2])
#
s2 = ce + hori - verti
s3 = ce + hori + verti
s4 = ce - hori + verti
s1 = ce - hori - verti
ce = np.append(ce,1)
s1 = np.append(s1,1) 
s2 = np.append(s2,1)
s3 = np.append(s3,1) 
s4 = np.append(s4,1) 
#print(s1)
# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.axis([-10,10,-10,10])

# Initialize the plot elements for the Sun and Earth (square)
sun_plot, = ax.plot([], [], '*b',)
ln, = ax.plot([], [], 'r')
center_dot, = ax.plot([], [], '.k')

# Initialize a list to store Earth's positions during the animation
ce_list = []
ce_list.append((ce,s1,s2,s3,s4))
cr_list = []
cr_list.append((s1,s2,s3,s4))

# Perform Earth's rotation and store positions
for i in ce_list:
    #print("i is:  ",i)
    ce = am.rotate_tuple(i, sun[0], sun[1], phi_rotate)
    #print(ce)
    #cr = am.rotate_tuple(cr_list,cs[0],cs[1],phi_rotate)
    ce_list.append(ce.copy())

    #cr_list.append(cr.copy())

# Function to initialize the animation
def init():
    sun_plot.set_data(sun[0], sun[1])
    center_dot.set_data(ce[0], ce[1])  # Initialize the center dot at the Earth's center
    return sun_plot, ln, center_dot

# Function to update the animation frame
def update(frame):
    ce_frame = ce_list[frame]
    square = np.stack([s1,s2,s3,s4])
    x_data,y_data = square[:,0],square[:,1]

    # Apply rotation to each vertex of the Earth's square separately
    ln.set_data(ce_frame[0] + x_data,
                ce_frame[1] + y_data)
    center_dot.set_data(ce_frame[0], ce_frame[1])
    return sun_plot, ln, center_dot

# Create the animation
ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10, blit=True)

# Display the animation
plt.show()
