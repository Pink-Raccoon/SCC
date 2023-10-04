# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:47:17 2021

@author: roor
"""

import matplotlib.pyplot as plt
import load_images as li

images = li.getImages()

plt.figure(1)
li.imshowRgb(images['Jetski'])

plt.figure(2)
li.imshowGray(images['Sunflowers'])
