import numpy as np
import load_data as ld


matrices = ld.loadData()
trainLabels1 = matrices['trainLabelsEx1']
trainLabels2 = matrices['trainLabelsEx2']
trainMatrixEx1 = matrices['trainMatrixEx1']
trainMatrixEx2 = matrices['trainMatrixEx2']

testLabels1 = matrices['testLabelsEx1']
testLabels2 = matrices['testLabelsEx2']
testMatrixEx1 = matrices['testLabelsEx1']
testMatrixEx2 = matrices['testLabelsEx2']

def train(matrix,trainlabels):
    # 1 = spam, 0 = non spam
    spams = np.where(trainlabels == 1)[0] # Indices of which rows in matrix are spam
    nonSpams = np.where(trainlabels == 0)[0] # Indices of which rows in matrix are non spam

    spamDocs = np.array([]).astype(int)
    nonSpamDocs = np.array([]).astype(int)
    #Because matrix is size (8,5)
    for k in spams:
        if(k >= 0 and k<= 7):
            spamDocs = np.append(spamDocs,k)
    for k in nonSpams:
        if(k >= 0 and k<= 7):
            nonSpamDocs = np.append(nonSpamDocs,k)
    totalSpam = len(spamDocs) # number of spam documents
    totalNonSpam = len(nonSpamDocs) #number of non spam documents
    probSpam = totalSpam / (totalSpam+totalNonSpam)
    numTokens = np.shape(matrix)[1]
    spamOccurences = np.sum(matrix[spamDocs],axis=0)
    nonSpamOccurences  = np.sum(matrix[nonSpamDocs],axis=0)
    totalSpamWords = np.sum(spamOccurences)
    totalNonSpamWords = np.sum(nonSpamOccurences)

    # print("total Spam documents: {}".format(totalSpam))
    # print("total non spam docs: {}".format(totalNonSpam))
    # print("train matrix {}".format(matrix))
    # print("spam Occurences {}".format(spamOccurences))
    # print("non spam occurences {}".format(nonSpamOccurences))
    # print("total spam word count {}".format(totalSpamWords))
    # print("total non spam word count {}".format(totalNonSpamWords))

    probTokensSpam = spamOccurences / totalSpamWords
    if len(probTokensSpam) < 11:
         print('probTokensSpam: ', probTokensSpam)
    probTokensNonSpam = nonSpamOccurences / totalNonSpamWords
    if len(probTokensNonSpam) < 11:
         print('probTokensNonSpam ', probTokensNonSpam)
    return probTokensSpam, probTokensNonSpam, probSpam, numTokens

# train(trainMatrixEx1,trainLabels1)
# train(trainMatrixEx2,trainLabels2)

