import numpy as np

from scipy.stats import multivariate_normal
import helper as hp

def classify_gmm(A, M, k):
    t = M.shape[0]
    r, d = A.shape
    N = r//k
    pd = np.zeros((t,k))
    alpha = np.zeros((M.shape[0],))
    for i in range(k):
        T_i = A[N*i:N*(i+1),:]
        m_i = np.mean(T_i,axis=0)
        print("means for i={} are: {} \n".format(i,m_i))
        cov_mat_i = np.cov(T_i.T)
        print("cov matrices for i={} are:  {} \n".format(i,cov_mat_i))
        prob_dens = multivariate_normal.pdf(M, mean=m_i,cov=cov_mat_i)
        pd[:, i] = prob_dens

    alpha=pd.argmax(axis=1)
    print("alpha is {} \n".format(alpha))

    return alpha
