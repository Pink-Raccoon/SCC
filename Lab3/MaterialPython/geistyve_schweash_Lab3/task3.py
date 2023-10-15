

import numpy as np
import load_images as li
import matplotlib.pyplot as plt
import auxiliary_methods as am

#a
images = li.getImages()
plt.figure(1)
original = li.imshowRgb(images['Jetski'])



gaussianfilt = am.gaussian_kernel(26,13)

filteredJetski = li.imfilter(images['Jetski'],gaussianfilt.reshape(1,-1))
plt.figure(2)
li.imshowRgb(filteredJetski)
plt.show()



#b
images = li.getImages()
plt.figure(1)
original = li.imshowRgb(images['Pinkflower'])

# Idea Gaussian Filter with a wide Sigma for more significant blurring but only for the diagonals of the matrix

filteredPinkflower = li.imfilter(images['Pinkflower'],diagonalfilt)

plt.figure(2)

plt.show()