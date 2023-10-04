import numpy as np
import load_images as li

images = li.getImages()
rgb = li.imshowRgb(images['Monroe'])

#a
filt = np.ones((9,9)) / 81
print(images['Monroe'])
print(li.imfilter(images['Monroe'],filt))



