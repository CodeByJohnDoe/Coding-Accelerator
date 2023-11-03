# see file
        
# Time = 2h + 1h (Fuck, wrong path for test.txt ..)
# Date = 1 & 3 novembre 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import found_extension

def see_file_exemple() :
    message_error = "error"
    g = len(sys.argv)
    
    if g >= 2 :
        for i in range (1,g) :
            argv = sys.argv[i]
                
            if found_extension(argv, "txt") == True :
                try :
                    with open(argv, 'r') as file :
                        print(file.read())
                except FileNotFoundError:
                    print(message_error)
    else :
        print(message_error)

see_file_exemple()