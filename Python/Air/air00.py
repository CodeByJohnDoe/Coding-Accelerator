# Split by markers
        
# Time = 3h
# Date = 4 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import split


def split_exemple() :
    message_error = "error"
    
    if len(sys.argv) == 2 :
        markers = [9,11,32] # HT VT Tab ASCII

        input_split = split(sys.argv[1], markers)
        
        for i in range (len(input_split)) :
            print(input_split[i])
        
    else :
        print(message_error)

split_exemple()