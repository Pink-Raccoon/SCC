import matplotlib.pyplot as plt
import load_images as li
import numpy as np

images = li.getImages()


plt.figure(1)
li.imshowGray(images['Testshapes'])


picture_data = images['Testshapes']


after_rotate = np.zeros_like(picture_data)

angle = np.pi / 6


def rotate_around_point(p_old, a, b, angle):
    aux_mat_1= np.array([[1,0,a],[0,1,b], [0,0,1]])
    aux_mat_2= np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0,0,1]])
    aux_mat_3= np.array([[1,0,-a], [0,1,-b], [0,0,1]])

    return aux_mat_1@aux_mat_2@aux_mat_3@p_old



def rotatePicture(Im, angle):
    a,b = np.shape(Im)
    centre_x = a/2
    centre_y = b/2

    
    after_rotate = np.zeros_like(Im)
    
    for i in range(a):
        for j in range(b):
            intOldPixel = images['Testshapes'][i,j]
            z = rotate_around_point(np.array([i, j, 1]), centre_x, centre_y, angle=angle)
            l= int(np.rint(z[0]))
            m = int(np.rint(z[1]))
            #print(type(l))
            if l < a and m < b and l > 0 and m > 0:
                after_rotate[l][m] = intOldPixel

    return after_rotate

pic1 = rotatePicture(images['Testshapes'], angle)

plt.figure(2)
li.imshowGray(pic1)



pic2 = li.medfilt2(pic1, 3)

plt.figure(3)
li.imshowGray(pic2)

plt.show()