import pathlib
from pathlib import Path
import os
import time


'''test pathlib object'''

obj_os = os.path.isdir(os.getcwd())
print(obj_os)
'''
obj_os_get = os.getcwd()
print(obj_os_get)
'''
p = Path.cwd()


print(p)
print(Path.cwd().is_dir())



