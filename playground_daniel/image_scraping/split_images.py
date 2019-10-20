import glob
import shutil

dir_dests = ["train"]*8 + ["val"] + ["test"]

files = sorted(glob.glob("jupiter_images/images_cropped/*.jpeg"))
for i in range(len(files)):
    dir_dest = dir_dests[i%len(dir_dests)]
    file_path = files[i]
    file = file_path.split('/')[-1]

    shutil.copyfile(file_path, f"../../cycle-gan-dataset/{dir_dest}B/{file}")


files = sorted(glob.glob("bing_earth_images/*.jpeg"))
for i in range(len(files)):
    dir_dest = dir_dests[i%len(dir_dests)]
    file_path = files[i]
    file = file_path.split('/')[-1]

    shutil.copyfile(file_path, f"../../cycle-gan-dataset/{dir_dest}A/{file}")


