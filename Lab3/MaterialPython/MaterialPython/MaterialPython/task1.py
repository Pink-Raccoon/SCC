def get_intensity(Im,i,j):
    for k,l in Im:
        if i <= k & j <= l :
            return Im[i,j]
        else:
            return 0.0
def myfilter(Im, F):
    N = 1
    n,m = np.shape(Im)
    k = -N
    l = -N
    R = np.zeros((n,m))
    x= 0
    
    for i,j in Im:
        intensity = get_intensity(Im,i,j)
        for i,j in Im:
            bla = Im(i+k,j+l) * F(N+k,N+l)
            while x < Im.len():
                R += bla
                x += 1

    return R

matrixF = np.array([[1,1,1],[1,1,1],[1,1,1]])* (1/9)
sunflower = getImages()
print(sunflower['Sunflowers'])