# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:31 2021

@author: roor
"""

import numpy as np
from sklearn.metrics import confusion_matrix


# supplied by the lecturer
def distance(p, q):
    dif = p - q
    return np.linalg.norm(dif, 2)


def classify_nearestmean(A, M, k):
    # classification by nearest mean
    t = M.shape[0]
    r, d = A.shape
    N = r//k

    means = np.zeros((k, d))
    alpha = np.zeros((M.shape[0],))
    for i in range(k):
        T = A[N*i:N*(i+1)]
        means[i, :] = np.mean(T, axis=0)
    # print(means)
    dist_to_mean = np.zeros((k,))
    for i in range(t):
        P = M[i, :]
        for j in range(k):
            dist_to_mean[j] = distance(P, means[j, :])
        alpha[i] = dist_to_mean.argmin()

    return alpha


def rgbImage2Matrix(img):
    d = img.shape[2]
    dims = img.shape[:2]
    return img.reshape(-1,d), dims

def vector2grayImage(M,dims):
    img = M.reshape(dims)
    return img

def error_rate(mask, result):
    mask = mask.flatten()
    result = result.flatten()
    
    confusion = confusion_matrix(mask,result)
    TP = confusion[1,1]
    TN = confusion[0,0]
    FP = confusion[0,1]
    FN = confusion[1,0]
    total = TP + TN + FP + FN
    print("error rate for image = {} \n".format((FN+FP)/total))
    print("false positive rate for image = {} \n".format(FP/(FP+TN)))
    print("false negative rate for image = {} \n".format(FN/(FN+TP)))