import numpy as np
import load_images as li

filt = np.ones((3,3))/9
test = np.array([[1,2,3],[4,5,6],[7,8,9]])


def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(
        lambda x: (1/ (2*np.pi*sigma**2)) * np.exp(-(x - (size-1)/2)**2 / (2*sigma**2)),
        (size,),
        dtype=float
    )
    return kernel / np.sum(kernel)
    

def traverse_matrix_diagonal(matrix):
   m = len(matrix)
   if m == 1: return matrix[0][0]
   for i in range(m):
       vlaue =matrix[i][-1-i]
   return matrix

matrix = [[10,5,9,6],[8,15,3,2],[3,8,12,3],[2,11,7,3],]
#print(traverse_matrix_diagonal(matrix))
        
        

#print(traverse_matrix_diagonal(test,filt))
print(gaussian_kernel(9,6))