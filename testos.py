import os
'''reference data : https://steam.oxxostudio.tw/category/python/library/os.html'''

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
'''print(os.listdir("demo"))'''
print(os.listdir())
print(os.listdir("demo"))

'''
os.chdir("D:/")
print(os.listdir())''''''print all dir in work space'''

'''os open file '''
file1 = os.open("demo/demo.txt", os.O_RDWR | os.O_CREAT)
file2 = os.open("use_os.txt", os.O_CREAT)

'''os close file'''
os.close(file1)
os.close(file2)

'''os write file'''
write_in_data = "hello world \nGood Morning!!!"
os_write_data = "demo by os write"

os.write(os.open("demo/demo.txt", os.O_RDWR),
         write_in_data.encode())
os.write(os.open("use_os.txt", os.O_RDWR),
         os_write_data.encode())
os.write(os.open("demo_change_name.txt", os.O_RDWR),
         os_write_data.encode())

'''os rename have file extension = file , not is folder'''
'''os.rename("useos.txt", "demo_change_name.txt")'''
'''os.rename("demo", "demo2")'''

'''os delete file'''
'''os.remove("demo")'''
'''os.remove("test.txt")'''
'''show dir'''
print(os.listdir())

'''os get file stat'''
'''print(os.stat("use_os.txt"))'''

'''os path'''
os_path = os.getcwd()

print(os.path.abspath("main.py"))
print(os.path.basename("main.py"))

print(os.path.exists("main.py"))
print(os.path.exists("testfile.txt"))

print(os.path.exists("demo"))
print(os.path.isdir("demo"))
print(os.path.isfile("demo"))

print(os.path.getctime("demo"))
print(os.path.getsize("main.py"))

print(os.path.basename(os_path))

'''os system'''
'''os.system("del demo")'''
'''os.system("cat use_os.txt")'''
