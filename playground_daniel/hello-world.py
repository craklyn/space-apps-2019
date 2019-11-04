import cv2
from glob import glob
import PIL
from PIL import Image
import numpy as np
import urllib.request

# Assumption: Directory contains only images.
def load_images(dir):
    for file in glob(dir + "/*"):
        pil_image = Image.open(file)

        # Let's only deal with color images.  Require three image dimensions (h, w, color) 
        if len(np.array(pil_image)) != 3:
            continue

        open_cv_image_rgb = np.array(pil_image.convert("RGB"))

        # Convert RGB to BGR 
        open_cv_image = open_cv_image_rgb[:, :, ::-1].copy()

def download_images(url):
    filename = url.split('/')[-1]

    urllib.request.urlretrieve(url, "image_scraping/" + filename[0:filename.index("?")] + ".jpeg")


def scrape_images():
    for x in range(0,3000):

        url = f"https://t.ssl.ak.dynamic.tiles.virtualearth.net/comp/ch/0212300302{str(x).zfill(4)}?mkt=en-US&it=A,G,RL&shading=hill&n=z&og=526&c4w=1&src=h"

        print(url)
        try:
            download_images(url)
        except urllib.error.HTTPError:
            continue
        except ValueError:
            continue

scrape_images()

def noisy(noise_typ,image):
    if noise_typ == "gauss":
        row,col,ch= image.shape
        mean = 0
        var = 50
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return np.clip(noisy.astype(int), 0, 255)
    elif noise_typ == "s&p":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i, int(num_salt))
                for i in image.shape]
        out[coords] = 255

        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i, int(num_pepper))
                for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ =="speckle":
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)*0.1
        gauss = gauss.reshape(row,col,ch)        
        noisy = image + image * gauss
        return np.clip(noisy.astype(int), 0, 255)


def chop_images(dir):

    for file in glob(dir + "/*.jpg"):
        print(file)
        image = cv2.imread(file)        

        N = 256
        M = 256
        tiles = [image[x:x+M,y:y+N] for x in range(0,image.shape[0],M) for y in range(0,image.shape[1],N)]

        for i in range(len(tiles)):
            tile = tiles[i]
            if tile.shape[0] == 256 and tile.shape[1] == 256:
#                cv2.imwrite(file + "_" + str(i) + ".jpeg" , tile)
#                print("gauss/" + file + "_" + str(i) + ".jpeg")
                cv2.imwrite("gauss/" + file + "_" + str(i) + ".jpeg" , noisy("gauss", tile))
                cv2.imwrite("snp/" + file + "_" + str(i) + ".jpeg" , noisy("s&p", tile))
                cv2.imwrite("speckle/" + file + "_" + str(i) + ".jpeg" , noisy("speckle", tile))

#chop_images("image_scraping/jupiter_images")
