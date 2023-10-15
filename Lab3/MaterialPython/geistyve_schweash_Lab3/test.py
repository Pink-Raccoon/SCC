import matplotlib.pyplot as plt
import load_images as li
import numpy as np
import task1 as t1


images = li.getImages()
plt.figure(1)
li.imshowGray(images['Sunflowers'])

test = np.ones((3,3)) /9
blurred_img = t1.myfilter(images['Sunflowers'],test)
plt.figure(2)
li.imshowGray(blurred_img)
plt.show()