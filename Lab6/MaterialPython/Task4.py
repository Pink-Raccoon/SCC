import numpy as np
import load_data as ld
import helper as hp
import Task2b as tk2
import matplotlib.pyplot as plt
from sklearn import svm

images = ld.load_data()
skin = images['skindata']
nonSkin = images['nonskindata']
test = images['test']
maskDat =images['maskTest']



N = 10000
d = 3



# print("Shape of skin:", skin.shape)
# print("Shape of nonSkin:", nonSkin.shape)
# print("Shape of maskDat:", maskDat.shape)



# print("Number of dimensions in maskDat:", maskDat.ndim)


testMatrix,testdims = hp.rgbImage2Matrix(test)
A = np.vstack([skin,nonSkin])
maskDat = maskDat.reshape(N,-1)
maskDat = maskDat[:2*N]



classifier = svm.SVC(kernel='linear')
classifier.fit(A, maskDat)
test_predictions = classifier.predict(testMatrix)

gmm_predictions = tk2.classify_gmm(A,testMatrix,2)

confusion_svm = hp.error_rate(maskDat, test_predictions)
confusion_gmm = hp.error_rate(maskDat, gmm_predictions)


