import os
'''test os object'''

'''get file's address
fileaddr = os.getcwd()
print("file browser at : " + fileaddr)
'''
print("file browser at : " + os.getcwd())

'''change work space'''
'''os.chdir("D:")'''

'''make dir'''
'''os.mkdir("demo")'''
'''os.mkdir("demo/hello.txt")under demo dir's hello.txt dir'''

'''delete dir'''
'''os.rmdir("demo")'''

'''list all file in dir with list'''
print(os.listdir("demo"))

