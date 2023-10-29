# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:34:44 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt


from sklearn.metrics import silhouette_score
from sklearn.mixture import BayesianGaussianMixture as bgm

from load_data import load_data
from plot_clusters import plot_clusters

plt.close('all')

dictData = load_data()


   



def cluster_gaussMixture(data):

    N, d = data.shape
    alpha = np.ones((N, 4))             # alpha[:, i] assignment when number
                                        # of clusters is i+2
    silhouetteValue = np.zeros((4,))    # silhoutteValue[i]: silhouette value
                                        # for alpha(:,i)
    for k in range(4):
        BGM = bgm(k+2).fit(data)
        alpha[:, k] = BGM.predict(data)
        silhouetteValue[k] = silhouette_score(data, alpha[:, k])

    i = silhouetteValue.argmax()        # finding index for optimal silhouette

    alphaOpt = alpha[:, i]

    return alphaOpt


for k in range(10):
    dataString = 'data{:d}'.format(k+1)
    data = dictData[dataString]

    alpha = cluster_gaussMixture(data)
    plot_clusters(data, alpha,k+1)
   
   #Task 4

   #Data4 now has two clusters instead of 6
   #Data 6 now has 4 clusters instead of two, which is ok the left and right cigar like clusters are separate at least and the one in the middle which is less dense in all directions was divided into additional two clusters
   #Data 9 now has the horizontal cigar as one complete cluster
   #Data 10 the nose is mostly now one cluster, just one point is clustered with the mouth