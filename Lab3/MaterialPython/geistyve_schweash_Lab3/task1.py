
import matplotlib.pyplot as plt
import load_images as li
import numpy as np


def get_intensity(Im, i, j):
    a, b = np.shape(Im)

    if i in range(0, a, 1) and j in range(0,b,1):
        return Im[i][j]
    else:
        return 0.

# Sum
def myfilter(Im, F):
    a,b = np.shape(Im)
    resultingImage = np.zeros((a,b))

    for c in range(a): # 0-a-1 Reihe 
        for d in range(b): # 0-b-1 Spalte
            j = 0
            
            for i in range(-1, 2, 1):
                for k in range(-1, 2, 1):
                    j += get_intensity(Im, c+i,d+k) * F[i+1][k+1]
            
            resultingImage[c,d] = j
    
    return resultingImage
