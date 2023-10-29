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
sun =      [0.0,0.0]                              # coordinates of the sun

n_per_day =  1
n_days =  365
n = n_days*n_per_day                            # number of iterations
phi_rotate =  2*np.pi / n_days / n_per_day      # angular velocity earth - sun
earth_rotate = 0.1

side_len = 0.8
tHori = np.array([side_len/2, 0])
tVerti = np.array([0,side_len/2])

s1 = ce - tHori - tVerti
s2 = ce + tHori - tVerti
s3 = ce + tHori + tVerti
s4 = ce - tHori + tVerti

ce = np.append(ce,1)
sun = np.append(sun,1)
s1 = np.append(s1,1) 
s2 = np.append(s2,1)
s3 = np.append(s3,1) 
s4 = np.append(s4,1) 

ce_list = [ce]
cr_list = []
cr_list.append(np.stack([s1,s2,s3,s4]))
# print("cr_list {}".format(cr_list))
# for i in range(n):
#     ce = am.rotate_around_point(ce,sun[0],sun[1],phi_rotate)
#     cr = am.rotate_tuple(cr_list[i][0:], ce[0],ce[1], earth_rotate)     
#     ce_list.append(ce)
#     cr_list.append(cr)             # generate coordinates
for i in range(n):
    ce = am.rotate_around_point(ce,sun[0],sun[1],phi_rotate)
    cr_ = am.rotate_tuple(cr_list[i][0:],sun[0],sun[1],phi_rotate) #square points around sun
    cr = am.rotate_tuple(cr_,ce[0],ce[1],earth_rotate) #rotating square around earth dot
    ce_list.append(ce)
    cr_list.append(cr) 

# Initialize the figure and axis
fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
center_dot, = plt.plot([], [], '.r')
earth_plot, = plt.plot([],[],'r')

def init():
    ax.axis([-10,10,-10,10])
    ax.set_aspect('equal', 'box')
  
    return center_dot, earth_plot,


def update(frame):
    ce_frame = ce_list[frame]
    cr_frame = cr_list[frame]
    center_dot.set_data(ce_frame[0],ce_frame[1])
    x = np.stack([cr_frame[0][0],cr_frame[1][0],cr_frame[2][0],cr_frame[3][0],cr_frame[0][0]])
    y = np.stack([cr_list[frame][0][1],cr_frame[1][1],cr_frame[2][1],cr_frame[3][1],cr_frame[0][1]])
    earth_plot.set_data(x,y)
    
    
    return center_dot, earth_plot,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
fig.show()
plt.show()
