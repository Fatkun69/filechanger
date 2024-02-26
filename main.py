import os
import glob
import pathlib

'''change file name program'''
''' hello world
'''

'''
print("hello world")
reference data : https://www.delftstack.com/zh-tw/howto/python/how-to-find-files-with-certain-extension-only-in-python/

'''

#target file format
#targetfileformat = [".nfo"]

'''
#file object
file = open("test.txt" , "r", encoding = "utf-8")
words = file.read()
print(words)

'''
'''
#reference data : https://ithelp.ithome.com.tw/articles/10262521
#create directory , have directory will error
os.mkdir(os.path.join("Folder1"))#root
os.mkdir(os.path.join("Folder1", "File1.txt"))#after root , add folder
os.mkdir(os.path.join("Folder1", "File2.csv"))
os.mkdir(os.path.join("Folder1", "File3.txt"))
os.mkdir(os.path.join("Folder1", "File1.txt", "TestSecond.txt"))#third folder
# all is folder , not file

'''
