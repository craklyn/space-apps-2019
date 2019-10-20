import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

from listOfInd import listOfInd

url = 'https://www.jpl.nasa.gov/spaceimages/index.php?search=2001+Mars+Odyssey'
response = requests.get(url)
soup = BeautifulSoup(response.text)
#
#
one_a_tag = soup.findAll('img')
base = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA'
suff='_hires.jpg'
names = []
for el in one_a_tag:
    
    link = el['src']
    ix = link.find('PIA')
    if (ix !=-1):
        idd=link[(ix+3):(ix+8)] #image ids #image ids
        download_url = base + idd + suff
        name = 'PIA'+idd
        fname = './MarsMissionImages/'+name+'.jpg'
        print(fname)
        names.append(fname)
        #urllib.request.urlretrieve(download_url,fname) 

    else:
        continue    
        

#%%Read and split images into tiles     
px=256
names = glob.glob('./MarsMissionImages/*')
for el in names:
    img = mpimg.imread(el)
    ix = el.find('PIA')
    idd=el[(ix+3):(ix+8)]
    name = 'PIA'+idd
    if name in ['PIA23205','PIA22738','PIA22519']:
        continue
    #plt.imshow(img,cmap='gray')
 
    m,n=img.shape
    indx = listOfInd(m,px)
    indy = listOfInd(n,px)
    k=0    
    for i in (indx):
        i = int(i)
        for j in indy:
#            plt.figure()
            
            j = int(j)
            arr = img[i:(i+px),j:(j+px)]
#            plt.imshow(arr)
            fname = ('./MarsMissionTiles/' + name + '_' + str(k) + '.jpg')
            print(fname)
            mpimg.imsave(fname,arr,cmap='gray')
            k+=1
#%%
   img = mpimg.imread(names[1])         
#%% Damage images  

names = glob.glob('./MarsMissionTiles/*')
for el in names:
    img = mpimg.imread(el)
    img = img[:,:,0]
    #plt.imshow(img,cmap='gray')  
    m,n=img.shape
    maxrow=5
    maxcol=6 
    z = np.zeros((maxrow,maxcol))
    istart = np.random.randint(0,(m-maxrow))
    jstart = np.random.randint(0,(n-maxcol))
    
    
    img_cp = img.copy()
    img_cp[istart:(istart+maxrow),jstart:(jstart+maxcol)]=0
    #plt.imshow(img_cp,cmap='gray')
    ix = el.find('PIA')
    ixx = el.find('.jpg')
    name=el[ix:ixx]
    
    fname = ('./MarsMissionTilesDamaged/' + name + '_damaged.jpg')            
    mpimg.imsave(fname,img_cp,cmap='gray')






#mynoise = np.random.normal(117,45,(5,4))
     
            
        
        

    
    
#url = 'https://images-assets.nasa.gov/image/PIA21288/PIA21288~orig.jpg'
#id = [‘21288’, ‘21005’, ‘04714’, ‘06388’, ‘10867’, ‘07162’, ‘11872’, ‘11323’, ‘11275’, ‘02078’, ‘04696’, ‘04844’, ‘07489’, ‘12381’, ‘09280’, ‘10052’, ‘16662’, ‘10036’, ‘10325’, ‘04751’, ‘10058’, ‘10806’, ‘11866’, ‘06842’, ‘04774’, ‘21004’, ‘20805’, ‘21177’, ‘21172’, ‘20982’, ‘20432’, ‘10022’, ‘06707’, ‘06810’, ‘05257’, ‘04699’, ‘06796’, ‘01159’, ‘06857’, ‘01505’, ‘05498’, ‘03051’, ‘10642’, ‘00801’, ‘10024’, ‘04901’, ‘04839’, ‘07163’, ‘16400’, ‘09093’, ‘09587’, ‘04636’, ‘04787’, ‘10023’, ‘10025’, ‘10635’, ‘05698’, ‘01046’, ‘03951’, ‘04975’, ‘05974’, ‘06931’, ‘10026’, ‘12394’, ‘21547’, ‘09120’, ‘09055’, ‘22993’, ‘05800’, ‘23370’, ‘09676’, ‘01695’, ‘06725’, ‘09495’, ‘18235’, ‘14168’, ‘03815’, ‘08609’, ‘00338’, ‘23335’, ‘00339’, ‘22397’, ‘23416’, ‘22621’, ‘03908’, ‘09127’, ‘13324’, ‘12875’, ‘18767’, ‘11892’, ‘14524’, ‘16248’, ‘01944’, ‘11893’, ‘13138’, ‘13712’, ‘19762’, ‘20260’, ‘18959’, ‘18684’]

#https://photojournal.jpl.nasa.gov/tiff/PIA23489.tif

#write a script to damage the images