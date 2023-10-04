# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

#idea: point around sun -> square around point rotates -> moon around earth

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
#import auxiliary_methods as am


def rotate_around_point(p_old, a, b, angle):
    aux_mat_1= np.array([[1,0,a],[0,1,b], [0,0,1]])
    aux_mat_2= np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0,0,1]])
    aux_mat_3= np.array([[1,0,-a], [0,1,-b], [0,0,1]])

    return aux_mat_1@aux_mat_2@aux_mat_3@p_old

def rotate_tuple(p1_old, p2_old, p3_old, p4_old, a, b, angle):
    p1_new = rotate_around_point(p1_old, a, b, angle)
    p2_new = rotate_around_point(p2_old, a, b, angle)
    p3_new = rotate_around_point(p3_old, a, b, angle)
    p4_new = rotate_around_point(p4_old, a, b, angle)

    return np.stack([p1_new, p2_new, p3_new, p4_new])

#print(rotate_around_point([2,5,1],6,9, math.pi/2))testing purposes
#print(rotate_around_point([-2, 8, 1], 5,7, math.pi))

ce =  np.array([0, 5, 1])                                  # start coordinates of earth
sun = np.array([0,0,1])                                    # coordinates of the sun

n_per_day =  1
n_days =  365
n = n_days*n_per_day                        # number of iterations
phi_rotate =  2* math.pi /n_days /n_per_day    # angular velocity earth - sun -> google
earth_rotate = 1  

# moon_around_earth = 1 #angular velocity moon -> earth

# moon_rotate = 1

# pm = np.array([0,7,1]) #initial position of the moon



e1 = np.array([-0.5, 4.5, 1])
e2 = np.array([0.5, 4.5, 1])
e3 = np.array([0.5, 5.5, 1])
e4 = np.array([-0.5, 5.5, 1])

# m1 = np.array([-0.5, 6.5, 1])
# m2 = np.array([0.5, 6.5, 1])
# m3 = np.array([0.5, 7.5, 1])
# m4 = np.array ([-0.5, 7.5, 1])



ce_list = [ce]
corners_list = []
corners_list.append(np.stack([e1,e2,e3,e4]))
print("cr_list {}".format(corners_list))

# pm_list = [pm]
# moon_list = []
# moon_list.append(np.stack([m1,m2,m3,m4]))

for i in range(n):
    ce = rotate_around_point(ce, sun[0], sun[1], phi_rotate)
    # pm = rotate_around_point(pm,ce[0], ce[1], moon_around_earth )
    
    new_points = rotate_tuple(corners_list[i][0],corners_list[i][1], corners_list[i][2], corners_list[i][3], ce[0],ce[1], earth_rotate)    
    ce_list.append(ce)                   # generate coordinates
    corners_list.append(new_points)
    
    # pm_list.append(pm)
    # new_moon_points = rotate_tuple(moon_list[i][0], moon_list[i][1], moon_list[i][2], moon_list[i][3], pm[0], pm[1], moon_rotate)
    # moon_list.append(new_moon_points)
    





fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
ln, = plt.plot([], [], 'or')
earth, = plt.plot([], [], 'r')
# moon_point, = plt.plot([], [],'.m')
# moon, = plt.plot([],[], 'b')


def init():
    ax.axis([-10, 10, -10, 10])
    ax.set_aspect('equal', 'box')
    return ln, earth, #moon_point, moon,


def update(frame):
    ln.set_data(ce_list[frame][0], ce_list[frame][1])
    a = np.stack([corners_list[frame][0][0],corners_list[frame][1][0],corners_list[frame][2][0],corners_list[frame][3][0],corners_list[frame][0][0]])
    b = np.stack([corners_list[frame][0][1],corners_list[frame][1][1],corners_list[frame][2][1],corners_list[frame][3][1],corners_list[frame][0][1]])    
    #this could have been solved a bit smoover i think
    earth.set_data(a, b) 
    # moon_point.set_data(pm_list[frame][0], pm_list[frame][1])

    # x = np.stack([moon_list[frame][0][0],moon_list[frame][1][0],moon_list[frame][2][0],moon_list[frame][3][0],moon_list[frame][0][0]])
    # y = np.stack([moon_list[frame][0][1],moon_list[frame][1][1],moon_list[frame][2][1],moon_list[frame][3][1],moon_list[frame][0][1]])
    # moon.set_data(x,y)
    return ln, earth, #moon_point,moon,



ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
plt.show()
