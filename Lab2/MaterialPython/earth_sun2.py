# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the coordinates of the Earth and the Sun
ce = np.array([5.0, 0.0, 1.0])  # Start coordinates of Earth
sun = np.array([0, 0, 1])       # Coordinates of the Sun
cs = np.array([5.0, 0.0, 1.0])
# Parameters for the animation
n_per_day = 1
n_days = 365
n = n_days * n_per_day          # Number of iterations
phi_rotate = 2 * np.pi / n_days / n_per_day  # Angular velocity earth - sun

# Side length of the square representing Earth
side_len = 1.0

# Coordinates of the vertices of the square representing Earth
earth_vertices = np.array([
    [-side_len / 2, -side_len / 2, 1],
    [side_len / 2, -side_len / 2, 1],
    [side_len / 2, side_len / 2, 1],
    [-side_len / 2, side_len / 2, 1],
     [-side_len / 2, -side_len / 2, 1] ,
])

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.axis([-10,10,-10,10])

# Initialize the plot elements for the Sun and Earth (square)
sun_plot, = ax.plot([], [], '*b',)
ln, = ax.plot([], [], 'r')
center_dot, = ax.plot([], [], '.k')

# Function to rotate a point around another point
def rotate_around_point(pOld, a, b, phi):
    rotMatr = np.array([[np.cos(phi), -np.sin(phi), 0],
                        [np.sin(phi), np.cos(phi), 0],
                        [0, 0, 1]])
    T1 = np.array([[1, 0, -a], [0, 1, -b], [0, 0, 1]])
    T2 = np.array([[1, 0, a], [0, 1, b], [0, 0, 1]])
    M = T2 @ rotMatr @ T1
    result = M @ pOld
    return result

def rotate_tuple(pList,a,b,phi):
    pRotated=[]
    

# Initialize a list to store Earth's positions during the animation
ce_list = [ce]

# Perform Earth's rotation and store positions
for i in range(n):
    ce = rotate_around_point(ce, sun[0], sun[1], phi_rotate)
    ce_list.append(ce.copy())

# Function to initialize the animation
def init():
    sun_plot.set_data(sun[0], sun[1])
    center_dot.set_data(cs[0], cs[1])  # Initialize the center dot at the Earth's center
    return sun_plot, ln, center_dot

# Function to update the animation frame
def update(frame):
    ce_frame = ce_list[frame]
    # Apply rotation to each vertex of the Earth's square separately
    ln.set_data(ce_frame[0] + earth_vertices[:, 0],
                ce_frame[1] + earth_vertices[:, 1])
    center_dot.set_data(ce_frame[0], ce_frame[1])
    return sun_plot, ln, center_dot

# Create the animation
ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10, blit=True)

# Display the animation
plt.show()
