# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import auxiliary_methods as am

ce =      [0.0,5.0]                             # start coordinates of earth
sun =     [0.0,0.0]                              # coordinates of the sun
cm =    [0.0,9.0]

n_per_day =  1
n_days =  365
n = n_days*n_per_day                           # number of iterations
earth_around_sun =  2*np.pi / n_days / n_per_day  # angular velocity earth - sun
earth_around_axis = 1
moon_around_earth = 2 * np.pi /27.3/ (1/27.3)
moon_around_axis = 2 * np.pi /27.3/ (1/27.3)

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

c1 = cm - mHori - mVerti
c2 = cm + mHori - mVerti
c3 = cm + mHori + mVerti
c4 = cm - mHori + mVerti

ce = np.append(ce,1)
sun = np.append(sun,1)
cm = np.append(cm,1)
s1 = np.append(s1,1) 
s2 = np.append(s2,1)
s3 = np.append(s3,1) 
s4 = np.append(s4,1) 

c1 = np.append(c1,1)
c2 = np.append(c2,1)
c3 = np.append(c3,1)
c4 = np.append(c4,1)

ce_list = [ce]
earthRotation_list = []
earthRotation_list.append(np.stack([s1,s2,s3,s4]))
cm_list = [cm]
moonRotation_list = []
moonRotation_list.append(np.stack([c1,c2,c3,c4]))
earth_and_moon_List = []


for i in range(n):    
    ce = am.rotate_around_point(ce,sun[0],sun[1],earth_around_sun)
    earthRotation_ = am.rotate_tuple(earthRotation_list[i][0:], sun[0],sun[1], earth_around_sun)  
    earthRotation = am.rotate_tuple(earthRotation_,ce[0],ce[1], earth_around_axis)

    cm_ = am.rotate_around_point(cm,ce[0],ce[1], moon_around_earth)  
    cm = am.rotate_around_point(cm_,sun[0],sun[1],earth_around_sun)
    moonRotation_ = am.rotate_tuple(moonRotation_list[i][0:],ce[0],ce[1],moon_around_earth) 
    moonRotation = am.rotate_tuple(moonRotation_,cm[0],cm[1],-moon_around_earth)
    moonRotationSun = am.rotate_tuple(moonRotation,sun[0],sun[1],earth_around_sun)

    

    ce_list.append(ce)
    earthRotation_list.append(np.stack(earthRotation) )    
    cm_list.append(cm) 
    moonRotation_list.append(np.stack(moonRotationSun) )
     # generate coordinates

# Initialize the figure and axis
fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
earth_dot, = plt.plot([], [], '.r')
earth_plot, = plt.plot([],[],'r')
moon_dot, = plt.plot([],[],'.k')
moon_plot,= plt.plot([],[],'k')


def init():
    ax.axis([-10,10,-10,10])
    ax.set_aspect('equal', 'box')
  
    return earth_dot, earth_plot, moon_dot, moon_plot,


def update(frame):
    ce_frame = ce_list[frame]
    cr_frame = earthRotation_list[frame]
    moon_frame = cm_list[frame]
    moonCorner_frame = moonRotation_list[frame]



    x = np.stack([cr_frame[0][0],cr_frame[1][0],cr_frame[2][0],cr_frame[3][0],cr_frame[0][0]])
    y = np.stack([earthRotation_list[frame][0][1],cr_frame[1][1],cr_frame[2][1],cr_frame[3][1],cr_frame[0][1]])

    x_moon = np.stack([moonCorner_frame[0][0],moonCorner_frame[1][0],moonCorner_frame[2][0],moonCorner_frame[3][0],moonCorner_frame[0][0]])
    y_moon = np.stack([moonCorner_frame[0][1],moonCorner_frame[1][1],moonCorner_frame[2][1],moonCorner_frame[3][1],moonCorner_frame[0][1]])
    
    moon_dot.set_data(moon_frame[0],moon_frame[1])
    earth_dot.set_data(ce_frame[0],ce_frame[1])
    moon_plot.set_data(x_moon,y_moon)    
    earth_plot.set_data(x,y)
    
    
   

    return earth_dot, earth_plot,moon_dot,moon_plot,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=50)
fig.show()
plt.show()
