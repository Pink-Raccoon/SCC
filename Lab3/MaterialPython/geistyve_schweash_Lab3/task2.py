
#%%
import numpy as np
import load_images as li
import matplotlib.pyplot as plt
#%%
#a
images = li.getImages()
plt.figure(1)
original = li.imshowGray(images['Monroe'])


filt = np.array([[0,0,0],[0,1,0],[0,0,0]]) - (np.ones((3,3))/9) + np.array([[0,0,0],[0,1,0],[0,0,0]]) #Sharpening filter that subtracts blurring from original and adds intermediate result to original
filteredMonroe = li.imfilter(images['Monroe'],filt)
plt.figure(2)
li.imshowGray(filteredMonroe)
plt.show()
# %%
#b
images = li.getImages()
plt.figure(1)
original = li.imshowGray(images['Airplane'])

plt.figure(2)
filteredAirplane = li.medfilt2(images['Airplane'],[3,3]) #Median filter to remove noise
li.imshowGray(filteredAirplane)
plt.show()
# %%
#c
images = li.getImages()
plt.figure(1)
original = li.imshowGray(images['Coins'])


filtSharp = np.array([[0,0,0],[0,1,0],[0,0,0]]) - (np.ones((3,3))/9) + np.array([[0,0,0],[0,1,0],[0,0,0]]) 
sharpenedCoins = li.imfilter(images['Coins'],filtSharp)

filtX = np.array([[-1,0,1],[-1,0,1],[1,0,-1]])
filtY = np.array([[1,1,1],[0, 0,0],[-1,-1,-1]])
filteredCoinsX = li.imfilter(sharpenedCoins,filtX) 
filteredCoinsY = li.imfilter(sharpenedCoins,filtY)

filteredCoins = filteredCoinsX+filteredCoinsY
plt.figure(2)
li.imshowGray(filteredCoins)
plt.show()

# %%
