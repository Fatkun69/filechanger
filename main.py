import os
import glob
import pathlib
import time

'''change file name program'''
'''
reference data : https://www.delftstack.com/zh-tw/howto/python/how-to-find-files-with-certain-extension-only-in-python/
'''

'''get now address'''
now_program_path = os.getcwd()
'''show path'''
print("work at : " + now_program_path)
print("show file in folder")
print(os.listdir(now_program_path))

'''set target path or file'''
'''print("select your target folder or file format")'''
file_target = input("select your target folder or file format : ")
print("select target : " + file_target)

'''check file exist'''


'''program exit with input 'exit' command'''
while (1):
    user_command = input("want to exit program , input 'exit' command :")
    if(user_command == 'exit'):
        print("exit Program")
        break
    else:
        print("program Run")

    '''end command if else'''

'''end while'''


