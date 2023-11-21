import numpy as np
from scipy.linalg import eigh
import load_data as ld
import helper as hp

data = ld.load_data()
datamat1 = data['dataMat1']

def getEigenvectors(dataMat,k):
    #Step 1: Preprocessing
    cov_mat = np.cov(dataMat.T)
    print("cov matrix is {}\n".format(cov_mat))
    eigen_vectors = eigh(cov_mat)
    np.flip(eigen_vectors[0])
    print("eigen vectors are {}".format(eigen_vectors))
    return eigen_vectors
    
getEigenvectors(datamat1,1)

def getMean(datamat):
    # #Step 2: Adjusting data
    mean = np.mean(datamat,axis=0)
    print("mean is {}\n".format(mean))
    return mean

def compressPCAImage(img,d,vEigen,imgM):
    return bla

# adjusted_matrix = dataMat - mean_vector
# print("adjusted matrix is {}\n".format())

# # Step 3: Transforming a data point
# column_vector = 

# #Step 4: Reprojecting back to the original coordinate system

# #Step 5: Add back mean!