import numpy as np
import load_data as ld
import helper as hp

images = ld.load_data()

skin = images['skindata']
nonSkin = images['nonskindata']
test = images['test']
maskDat =images['maskTest']

testMatrix,testdims = hp.rgbImage2Matrix(test)



A = np.vstack([skin,nonSkin])
r,s,t = test.shape

img = hp.classify_nearestmean(A,testMatrix,2)

R1 = hp.vector2grayImage(img,testdims)

#then plot (imshowgray)