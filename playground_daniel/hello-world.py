import cv2
from glob import glob
import PIL
from PIL import Image
import numpy as np


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
