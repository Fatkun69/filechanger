import os
import glob

folder_name = []
#print(glob.glob(os.path.join("*")))

#show file address now
print(os.getcwd())


'''get list data and store in list variable'''
folder_name = glob.glob(os.path.join("*"))

#folder_name.append(glob.glob(os.path.join("*")))
#print("folder name : " + str(folder_name))

#print(glob.glob(os.path.join("Folder1", "*")))

print("list folder name : " + str(folder_name))

