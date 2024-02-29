import os
import glob
import pathlib
import time

'''change file name program'''
'''
reference data : https://www.delftstack.com/zh-tw/howto/python/how-to-find-files-with-certain-extension-only-in-python/
'''

'''program exit with input 'exit' command'''
while 1:
    user_command = input("want to exit program , input 'exit' command :")
    if user_command == 'exit':
        print("exit Program")
        break
    else:
        print("program Run")

        '''get now address'''
        now_program_path = os.getcwd()

        '''show path'''
        print("work at : " + now_program_path)
        print("show file in folder under")
        '''print(os.listdir(now_program_path))'''
        list_folder_data = os.listdir(now_program_path)
        '''show file in vector line'''
        for i in list_folder_data:
            print(i)
        '''end for i'''

        '''set target path or file'''
        '''print("select your target folder or file format")'''
        file_target = input("select your target folder or file format : ")
        print("select target : " + file_target)

        '''check file exist'''
        '''flag use bool variable'''
        file_exists_flag = False
        '''default is no'''
        '''search file loop'''
        while 1:
            if os.path.exists(file_target):
                '''true exit'''
                file_exists_flag = True
                print("file already exists")
                break
            else:
                print("don't have target file")
                user_command = input("don't want to select file or target , input 'exit' command to exit : ")
                if user_command == 'exit':
                    print("do not select file and exit")
                    break
                else:
                    '''search file again'''
                    file_target = user_command
                '''end change user command if'''
            '''end if else'''

        '''end while 1'''

    '''check flag status'''
    if file_exists_flag:
        print('file exists')
    else:
        print('do not have file')

    '''end if else'''

'''end while'''

'''show message'''
print("Before exit program show message under")
print("This program is written by Handsome ken")
print("米奇米奇操你媽")
