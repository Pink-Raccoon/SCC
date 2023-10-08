

import numpy as np
import load_images as li
import matplotlib.pyplot as plt

#a
images = li.getImages()
plt.figure(1)
original = li.imshowRgb(images['Jetski'])

def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(
        lambda x: (1/ (2*np.pi*sigma**2)) * np.exp(-(x - (size-1)/2)**2 / (2*sigma**2)),
        (size,),
        dtype=float
    )
    return kernel / np.sum(kernel)
    
def gaussian_kernel_2d(size, sigma_x, sigma_y):
    kernel = np.fromfunction(
        lambda x, y: (1/ (2*np.pi*sigma_x*sigma_y)) * np.exp(-((x - (size-1)/2)**2 / (2*sigma_x**2) + (y - (size-1)/2)**2 / (2*sigma_y**2))),
        (size, size),
        dtype=float
    )
    return kernel / np.sum(kernel)
gaussianfilt = gaussian_kernel(26,13)

filteredJetski = li.imfilter(images['Jetski'],gaussianfilt.reshape(1,-1))
plt.figure(2)
li.imshowRgb(filteredJetski)
plt.show()



#b
images = li.getImages()
plt.figure(1)
original = li.imshowRgb(images['Pinkflower'])

diagonalFilt = gaussian_kernel_2d(30,5,5)

filteredFlower = li.imfilter(images['Pinkflower'],diagonalFilt)
plt.figure(2)
li.imshowRgb(filteredFlower)
plt.show()