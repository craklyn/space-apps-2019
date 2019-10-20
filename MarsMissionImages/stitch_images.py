from glob import glob
import numpy as np
import cv2


files = sorted(glob("MarsMissionTiles/*.jpg"))

dests = ["train/"]*8 + ["val/", "test/"]


for i in range(len(files)):
    file_path = files[i]
    file = file_path.split("/")[-1]
    dest = dests[i % len(dests)]

    image_good = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    image_damaged = cv2.imread("MarsMissionTilesDamaged/" + file.split(".")[0] + "_damaged.jpg", cv2.IMREAD_GRAYSCALE)

    # Require at least 10% of pixels to be brighter than 10/256 in order to alow into dataset
    if np.sum(np.greater(image_good, 10)) < image_good.shape[0]*image_good.shape[1]*0.1:
        continue

    images_both = np.concatenate((image_good, image_damaged), axis=1)
    cv2.imwrite("MarsMissionTilesCombined/" + file, images_both)
    cv2.imwrite("../pix2pix-dataset/" + dest + file, images_both)


