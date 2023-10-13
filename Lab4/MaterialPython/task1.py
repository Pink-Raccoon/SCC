import numpy as np
import load_data as ld

matrices = ld.loadData()
trainLabels = matrices['trainLabels']
trainMatrixEx1 = matrices['trainMatrixEx1']

# 1 = spam, 0 = non spam
spams = np.where[trainLabels == 1][0]
nonSpams = np.where[trainLabels == 0][0]

def computeProbability(case,matrix):
    spamTotalWords = np.size(spams)
    nonSpamTotalWords = np.size(nonSpams)


    return result



# print(computeProbability(trainMatrixEx1))

# print(probTokensSpam[0])
print(trainLabels)