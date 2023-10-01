# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:01:45 2021

@author: roor
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')


def init():
    # ax.axis('equal')
    ax.axis([0, 2*np.pi, -1, 1])
    ax.set_aspect('equal', 'box')
    # ax.set_xlim(0, 2*np.pi)
    # ax.set_ylim(-1, 1)
    return ln,


def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    # xdata = frame
    # ydata = np.sin(frame)
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 64),
                    init_func=init, interval=1000, repeat=False)
plt.show()
