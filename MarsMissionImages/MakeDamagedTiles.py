import requests
import urllib.request
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

from listOfInd import listOfInd

names = glob.glob('./MarsMissionTiles/*')
for el in names:
    img = mpimg.imread(el)
    img = img[:,:,0]
    #plt.imshow(img,cmap='gray')
    m,n=img.shape
    maxrow=5
    maxcol=6

    img_cp = img.copy()
    for _ in range(32):
        z = np.zeros((maxrow,maxcol))
        istart = np.random.randint(0,(m-maxrow))
        jstart = np.random.randint(0,(n-maxcol))

        img_cp[istart:(istart+maxrow),jstart:(jstart+maxcol)]=0

    #plt.imshow(img_cp,cmap='gray')
    ix = el.find('PIA')
    ixx = el.find('.jpg')
    name=el[ix:ixx]

    fname = ('./MarsMissionTilesDamaged/' + name + '_damaged.jpg')
    mpimg.imsave(fname,img_cp,cmap='gray')

