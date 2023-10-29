import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from scipy.stats import multivariate_normal
import helper as hp

def classify_gmm(A, M, k):
    t = M.shape[0]
    r, d = covA.shape
    N = r//k
    pd = np.zeros((t,k))
    alpha = np.zeros((M.shape[0],))
    for i in range(k):
        T = covA[N*i:N*(i+1)]

        alpha[i]=probDens.argmin()

    return alpha
