

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

diagonalfilt = np.array([[ 0,0,0.3194335],[ 0,0.36113301,0],[ 0,0,0.3194335]])

filteredPinkflower = li.imfilter(images['Pinkflower'],diagonalfilt)

plt.figure(2)
li.imshowRgb(diagonalfilt)
plt.show()