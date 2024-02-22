import os
import glob

folder_name = []
print(glob.glob(os.path.join("*")))
folder_name.append(glob.glob(os.path.join("*")))
print("folder name : " + str(folder_name))

print(glob.glob(os.path.join("Folder1", "*")))