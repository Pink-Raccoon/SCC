import numpy as np
import helper as hp
import load_data as ld

import Task2b as tk2

testData = ld.load_data()

A1 = testData['A1']
M1 = testData['M1']

A2 = testData['A2']
M2 = testData['M2']

tk2.classify_gmm(A1,M1,3)
tk2.classify_gmm(A2,M2,2)

images = ld.load_data()
