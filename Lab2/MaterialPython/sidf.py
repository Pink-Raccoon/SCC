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
sun =     [0.0,0.0]                              # coordinates of the sun
moon =    [0.0,9.0]

n_per_day =  1
n_days =  365
n = n_days*n_per_day                           # number of iterations
earth_around_sun =  2*np.pi / n_days / n_per_day  # angular velocity earth - sun
earth_around_axis = 1
moon_around_earth = 2 * np.pi / (n/12) 
moon_around_axis = 2 * np.pi /(n/12)

side_len = 1.0
side_moon = 0.6
tHori = np.array([side_len/2, 0])
tVerti = np.array([0,side_len/2])
mHori = np.array([side_moon/2,0])
mVerti = np.array([0,side_moon/2])

s1 = ce - tHori - tVerti
s2 = ce + tHori - tVerti
s3 = ce + tHori + tVerti
s4 = ce - tHori + tVerti

c1 = moon - mHori - mVerti
c2 = moon + mHori - mVerti
c3 = moon + mHori + mVerti
c4 = moon - mHori + mVerti

ce = np.append(ce,1)
sun = np.append(sun,1)
moon = np.append(moon,1)
s1 = np.append(s1,1) 
s2 = np.append(s2,1)
s3 = np.append(s3,1) 
s4 = np.append(s4,1) 

c1 = np.append(c1,1)
c2 = np.append(c2,1)
c3 = np.append(c3,1)
c4 = np.append(c4,1)

ce_list = [ce]
cr_list = []
cr_list.append(np.stack([s1,s2,s3,s4]))
moon_list = [moon]
moonCorner_list = []
moonCorner_list.append(np.stack([c1,c2,c3,c4]))


for i in range(n):    
    ce = am.rotate_around_point(ce,sun[0],sun[1],earth_around_sun)
    moon = am.rotate_around_point(moon,ce[0],ce[1], -moon_around_earth)  
    cr = am.rotate_tuple(cr_list[i][0:], ce[0],ce[1], earth_around_axis)  
    moonCorner = am.rotate_tuple(moonCorner_list[i][0:],moon[0],moon[1],moon_around_axis)     
    cr_list.append(cr) 
    moonCorner_list.append(moonCorner) 
    moon_list.append(moon) 
    ce_list.append(ce) # generate coordinates

# Initialize the figure and axis
fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
earth_dot, = plt.plot([], [], '.r')
earth_plot, = plt.plot([],[],'r')
moon_dot, = plt.plot([],[],'.k')
moon_plot,= plt.plot([],[],'k')
# New variable to track the Moon's rotation angle
moon_rotation_angle = 0.0

def init():
    ax.axis([-10, 10, -10, 10])
    ax.set_aspect('equal', 'box')
    return earth_dot, earth_plot, moon_dot, moon_plot

def update(frame):
    global moon_rotation_angle  # Declare the variable as global to update it
    ce_frame = ce_list[frame]
    cr_frame = cr_list[frame]
    moon_frame = moon_list[frame]
    
    # Update the Moon's position in its orbit around the Earth
    ce_frame = am.rotate_around_point(ce_frame, sun[0], sun[1], earth_around_sun)
    
    # Update the Moon's rotation around its own axis
    moon_rotation_angle += moon_around_axis * (1 / 60)  # Update based on frame rate
    
    # Calculate the rotation matrix for the Moon's rotation
    rotation_matrix = np.array([[np.cos(moon_rotation_angle), -np.sin(moon_rotation_angle)],
                                [np.sin(moon_rotation_angle), np.cos(moon_rotation_angle)]])
    
    # Apply the rotation matrix to the Moon's position
    moon_frame[0:2] = np.dot(rotation_matrix, moon_frame[0:2])
    
    earth_dot.set_data(ce_frame[0], ce_frame[1])
    x = np.stack([cr_frame[0][0], cr_frame[1][0], cr_frame[2][0], cr_frame[3][0], cr_frame[0][0]])
    y = np.stack([cr_frame[0][1], cr_frame[1][1], cr_frame[2][1], cr_frame[3][1], cr_frame[0][1]])
    earth_plot.set_data(x, y)
    moon_dot.set_data(moon_frame[0], moon_frame[1])
    
    return earth_dot, earth_plot, moon_dot

ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
fig.show()
plt.show()
