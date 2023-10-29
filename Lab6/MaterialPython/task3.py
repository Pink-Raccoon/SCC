import numpy as np
import load_data as ld
import helper as hp
import Task2b as tk2
import matplotlib.pyplot as plt

images = ld.load_data()

skin = images['skindata']
nonSkin = images['nonskindata']
test = images['test']
maskDat =images['maskTest']
# print("shape mask: {}".format(np.shape(maskDat)))
testMatrix,testdims = hp.rgbImage2Matrix(test)



A = np.vstack([skin,nonSkin])


img = hp.classify_nearestmean(A,testMatrix,2)
R1 = hp.vector2grayImage(img,testdims)
binary_img1 = (R1 > 0).astype(int) #Skin = 1, non-skin = 0
error1 = hp.error_rate(maskDat,binary_img1)
# print("shape of img1: {}".format(np.shape(binary_img1)))

img2 = tk2.classify_gmm(A,testMatrix,2)
R2 = hp.vector2grayImage(img2,testdims)
binary_img2 = (R2 > 0).astype(int)
error2 = hp.error_rate(maskDat,binary_img2)
# print("shape of img2: {}".format(np.shape(binary_img2)))



plt.figure(1)
plt.imshow(binary_img1,cmap='gray')


plt.figure(2)
plt.imshow(binary_img2,cmap='gray')



plt.show()

# Answer 3b)
'''
Evalutation of the results:
The nearest mean method does not identify the shadowy part of the hand as skin and erronously interprets the white shirt as part of the skin too.
Leading to the conclusion that the value of the white shirt is too close to the skin value.
However it does not not interpret much of the leaves as skin.
The gmm method interprets skin correctly, however also a large part of the leaves too.
'''