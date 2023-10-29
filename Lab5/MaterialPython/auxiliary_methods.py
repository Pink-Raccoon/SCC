import numpy as np
import load_data as ld

def V(I):
    row,column = np.shape(I)
    print(np.shape(I))
    np.reshape(I,(6,1))
    return I
Test = np.array([[1,2,3],[4,5,6]])
print(V(Test))
