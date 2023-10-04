import numpy as np
import math

# Function to rotate a point around another point
def rotate_around_point(pOld, a, b, phi):
    rotMatr = np.array([[np.cos(phi), -np.sin(phi), 0],
                        [np.sin(phi), np.cos(phi), 0],
                        [0, 0, 1]])
    T1 = np.array([[1, 0, -a], [0, 1, -b], [0, 0, 1]])
    T2 = np.array([[1, 0, a], [0, 1, b], [0, 0, 1]])
    M = T2 @ rotMatr @ T1
    result = M @ pOld
    return result

def rotate_tuple(pList, a, b, phi):
    pRotated = []
    for p in pList:
        pRotated.append(rotate_around_point(p, a, b, phi))
    return np.stack(pRotated)