import sys
import os
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import *
path = "/home/uf/Desktop/Coding Accelerator/Python"
    
check_list_files_names = []
files = os.listdir(path)

    
print(files)
print(len(files))