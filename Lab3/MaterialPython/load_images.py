# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:31 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
import scipy.signal as si
import os


def rgb2gray(img):
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])


def imshowGray(img):
    plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)


def imshowRgb(img):
    plt.imshow(img)


def imfilter(img, filt):
    return nd.convolve(img, filt, mode='nearest')  # mimicks imfilter of MATLAB


def medfilt2(img, size):
    return si.medfilt2d(img, kernel_size=size)    # mimicks medfilt2d of MATLAB


def getImages():
    img = {}

    Sunflowers = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics', 'sunflowers.png'))
    #Sunflowers = plt.imread('Pics\\sunflowers.png')
    img['Sunflowers'] = rgb2gray(Sunflowers)

    Monroe = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics','monroe.png'))
    #Monroe = plt.imread('Pics\\monroe.png')
    img['Monroe'] = rgb2gray(Monroe)

    Airplane = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics','airplane.png'))
    #Airplane = plt.imread('Pics\\airplane.png')
    img['Airplane'] = rgb2gray(Airplane)

    Coins = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics','coins.png'))
    #Coins = plt.imread('Pics\\coins.png')
    img['Coins'] = rgb2gray(Coins)

    Testshapes = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics','testshapes.png'))
    #Testshapes = plt.imread('Pics\\testshapes.png')
    img['Testshapes'] = rgb2gray(Testshapes)

    #img['Jetski'] = plt.imread('Pics\\jetski.png')
    Jetski = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics','jetski.png'))
    #img['Jetski'] = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics','jetski.png'))
    img['Jetski'] = rgb2gray(Jetski)
  
    Pinkflower = plt.imread(os.path.join(os.getcwd(), 'MaterialPython', 'Pics','pinkflower.png'))
    #img['Pinkflower'] = plt.imread('Pics\\pinkflower.png')
    img['Pinkflower'] = rgb2gray(Pinkflower)

    return img
