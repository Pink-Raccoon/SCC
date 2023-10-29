import numpy as np




def grayscaleImage2Vector(I):
    # Get the dimensions of the input image
    dims = I.shape

    # Reshape the image to a 1D vector by concatenating its rows
    vector = I.flatten()

    return vector, dims


def vector2GrayscaleImage(V, dims):
    r, s = dims  # Extract the dimensions from the 'dims' input

    # Reshape the vector into an r x s matrix
    I = V.reshape(r, s)

    return I

