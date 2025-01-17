# -*- coding: utf-8 -*-

def calculate_border_task1(path_img, crop_factor, sigma):

    """
    This function does the following:
    1) reads the picture stored at 'path_img' using cv2.imread and displays it
       using plt.imshow
    2) converts the color picture into a grey-scale picture using cv2.cvtColor
       and shows it
    3) cuts away the sides of the grey-scale image, the fraction is defined by
       'crop_factor'
    4) blurs the picture using a Gaussian filter (using cv2.GaussianBlur) with
       'sigma'; the larger sigma, the more the image gets blurred and finer
       contours disappear; this is necessary to get rid of noise and unwanted
       structures like hairs
    5) uses Otsu's method to turn the filtered grey-scale image into a binary
       image (using cv2.threshold)
    6) uses ndimage.binary_fill_holes() to fill holes in the binary picture 
       an cv2.connectedComponents() to keep only the region with the largest area
    7) uses cv2.findContours to calculate the border (aka contour) of the identified
       area and plots everything
    Input :  path_img         : path to color image (string)
             crop_factor      : percentage that should be cut away from 
                                image (e.g. 0.1 means 10%)
             sigma            : used for the Gaussian filter to blur the image
                                (e.g. 5) in imgaussfilt.m
    Output : cropped_img_cl  : cropped color image (sides are cut away)
             cropped_img_gs  : cropped grey scale image
             cropped_img_mask: logical array with mask of the lesion, i.e.
                               every pixel within the lesion has a value of 1, 
                               every pixel outside the lesion has a value of 0
             border          : array with x and y coordinates of the boundaries
                               of the lesion
    Remarks: Requires Installation of OpenCV (e.g. for Anaconda see https://www.geeksforgeeks.org/set-opencv-anaconda-environment/)
             enter the following in the Anaconda prompt: onda install -c menpo opencv
             Tutorial for Contour Detection: https://learnopencv.com/contour-detection-using-opencv-python-c/
    Example: [cr_img_cl,cr_img_gs,cr_img_mask,border] = calculate_border_task1_solution('B496a.png', 0.1, 5);
    Date: Nov, 1, 2021, knaa
    """
    import numpy as np
    from scipy import ndimage
    import matplotlib.pyplot as plt
    import cv2
    
# 1) Read image I1 in a using cv2.imread and plt.imshow and show in a subplot(2,3,1). 
#    Attention: CV2 reads picture as BGR (not RGB), and therefore, the image has to 
#    be converted with cv2.cvtColor(I1,cv2.COLOR_BGR2RGB)


    """ ... YOUR CODE COMES HERE ... """
    I1 = cv2.imread(path_img)
   
    # plt.subplot(2,3,1)
    # plt.imshow(I1)
    # plt.show()
# 2) Convert to grey scale using cv2.cvtColor with the code cv2.COLOR_BGR2GRAY
#    and show in a subplot(2,3,2)


    """ ... YOUR CODE COMES HERE ... """

    I1_gray = cv2.cvtColor(I1,cv2.COLOR_BGR2GRAY)
    plt.subplot(2,3,2)
    plt.imshow(I1_gray,cmap='gray')
    # plt.show()
# 3) Cutt away the given percentage on each side, e.g. crop_factor = 0.1;
#    and show in a subplot(2,3,3)


    """ ... YOUR CODE COMES HERE ... """
    shape = np.shape(I1_gray)
    xrange = np.int64([crop_factor*shape[0],(1-crop_factor)*shape[0]])
    yrange = np.int64([crop_factor*shape[1],(1-crop_factor)*shape[1]])
    
    I1_cropped = np.copy(I1[xrange[0]:xrange[1],yrange[0]:yrange[1],:])
    I1_gray_cropped = np.copy(I1_gray[xrange[0]:xrange[1],yrange[0]:yrange[1]])
    plt.subplot(2,3,3)
    plt.imshow(I1_gray_cropped,cmap='gray')
    # plt.show()

# 4) Filter using a Gaussian Filter with cv2.GaussianBlur and a high enough sigma (e.g. sigma = 5) to blur
#     and show in a subplot(2,3,4)


    """ ... YOUR CODE COMES HERE ... """
    I1_gray_cropped_blurred = cv2.GaussianBlur(I1_gray_cropped,ksize=(0,0),sigmaX=sigma,sigmaY=sigma,borderType=cv2.BORDER_REPLICATE)
    plt.subplot(2,3,4)
    plt.imshow(I1_gray_cropped_blurred,cmap='gray')
    # plt.show()

# 5) Convert to binary picture using Otsu's threshold method using cv2.threshold() with cv2.THRESH_BINARY+cv2.THRESH_OTSU
#    and show in a subplot(2,3,5), see
#    https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html


    """ ... YOUR CODE COMES HERE ... """ 
    ret,I1_gray_cropped_blurred_binary = cv2.threshold(I1_gray_cropped_blurred,0,1,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    plt.subplot(2,3,5)
    plt.imshow(I1_gray_cropped_blurred_binary,cmap='gray')
    # plt.show()

# 6) Fill holes in the image and keep only the largest area
#    using ndimage.binary_fill_holes() and cv2.connectedComponents() and show in a subplot(2,3,6)
#    You will have to swap black and white in the binary picture, e.g. IG5 = -IG4+1
    

    """ ... YOUR CODE COMES HERE ... """
    
    I1_swapped = -I1_gray_cropped_blurred_binary +1
    I1_gray_cropped_blurred_binary_filledHoles = ndimage.binary_fill_holes(I1_swapped)
    ret,labels = cv2.connectedComponents(I1_gray_cropped_blurred_binary_filledHoles.astype(np.uint8))

    I1_swapped = -I1_gray_cropped_blurred_binary+1
    IG6 = ndimage.binary_fill_holes(I1_swapped.astype(np.uint8))
    ret, labels = cv2.connectedComponents(IG6.astype(np.uint8))
    sum_max_area = 0
    IG7 = np.array(labels)

    for label in range(1,ret):
        mask = np.array(labels)
        mask[labels == label] = 255
        mask[labels != label]= 0
        if np.sum(mask) > sum_max_area:
            sum_max_area=np.sum(mask)
            IG7=mask
# 7) Compute the contours using cv2.findContours() with cv2.RETR_TREE and cv2.CHAIN_APPROX_NONE


    """ ... YOUR CODE COMES HERE ... """
    
    contours, hierarchy = cv2.findContours(IG7.astype(np.uint8),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #plotting
    for data in contours:
        print("The contours have this data %r" %data)
    im = IG7.astype(np.uint8)
    cv2.drawContours(im,contours,-1,(255,255,0),4)
    plt.subplot(2,3,6)
    plt.imshow(im,cmap='gray')
    
   

# Define output

    cropped_img_cl = I1_cropped
    cropped_img_gs = I1_gray_cropped
    cropped_img_mask = I1_swapped
    border = contours
    plt.show()
    return cropped_img_cl,cropped_img_gs,cropped_img_mask,border

calculate_border_task1("./B496a.png",0.1,5)