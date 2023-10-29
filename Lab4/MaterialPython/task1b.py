import numpy as np
import load_data as ld

matrices = ld.loadData()
trainLabels = matrices['testLabels']
trainMatrixEx1 = matrices['testMatrixEx1']

def test(matrix):
    