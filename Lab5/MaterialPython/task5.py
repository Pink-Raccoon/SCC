import matplotlib.pyplot as plt
import auxiliary_methods as am
import numpy as np
import load_data as ld
from sklearn.cluster import KMeans


images = ld.load_data()
moon = ld.rgb2gray(images['moon'])

plt.figure(1)
ld.imshowGray(moon)

vectorMoon, dimsMoon = am.grayscaleImage2Vector(moon)
vectorMoon =  vectorMoon.reshape(-1, 1)
print(dimsMoon)

kmeans = KMeans(n_clusters=2,random_state=0).fit(vectorMoon)

alpha = kmeans.predict(vectorMoon)


color_c1 = 0  # Black
color_c2 = 255  # White


cluster_pixels = {0: color_c1, 1: color_c2}


pixels_vectors = [cluster_pixels[alpha] for alpha in alpha]


clustered_image = am.vector2GrayscaleImage(np.array(pixels_vectors), dimsMoon)


plt.figure(2)
ld.imshowGray(clustered_image)

plt.show()