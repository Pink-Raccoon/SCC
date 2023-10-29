import numpy as np
import load_data as ld
import task1 as tk


matrices = ld.loadData()
trainLabels1 = matrices['trainLabelsEx1']
trainLabels2 = matrices['trainLabelsEx2']
trainMatrixEx1 = matrices['trainMatrixEx1']
trainMatrixEx2 = matrices['trainMatrixEx2']

testLabels1 = matrices['testLabelsEx1']
testLabels2 = matrices['testLabelsEx2']
testMatrixEx1 = matrices['testLabelsEx1']
testMatrixEx2 = matrices['testLabelsEx2']

# probTokensSpam, probTokensNonSpam, probSpam, numTokens = tk.train(trainMatrixEx1,trainLabels1)
probTokensSpam, probTokensNonSpam, probSpam, numTokens = tk.train(trainMatrixEx2,trainLabels2)
def test(matrix, testlabels):
    numberOfDocs = len(matrix)
    pMailSpam = np.zeros(numberOfDocs)
    pMailNonSpam = np.zeros(numberOfDocs)
    output = []

    for i in range(numberOfDocs):
        occurencesDoc = matrix[i]
        prod1 = 1
        prod2 = 1

        for j in range(numTokens):
            prod1 *= probTokensSpam[j] ** occurencesDoc
            prod2 *= probTokensNonSpam[j] ** occurencesDoc

        pMailSpam[i] = prod1
        pMailNonSpam[i] = prod2

        PmailAndSpam = pMailSpam * probSpam
        PmailAndNonSpam = pMailNonSpam * (1 - probSpam)
        
    classification = (PmailAndSpam > PmailAndNonSpam).astype(int)  # 1 for spam, 0 for non-spam
    output.append(classification)

    error_rate = sum(testlabels != output)/numberOfDocs
    print("Output: {}".format(output))
    print("Error rate: {}".format(error_rate))


#test(testMatrixEx1, testLabels1)
test(testMatrixEx2,testLabels2)
