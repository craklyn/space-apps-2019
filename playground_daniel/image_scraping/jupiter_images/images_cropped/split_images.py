import glob
import shutil

files = sorted(glob.glob("*.jpeg"))
dir_dests = ["train"]*8 + ["val"] + ["test"]

for i in range(len(files)):
    file = files[i]
    dir_dest = dir_dests[i%len(dir_dests)]
    shutil.copyfile(file, f"../../../../cycle-gan-dataset/{dir_dest}B/{file}")


