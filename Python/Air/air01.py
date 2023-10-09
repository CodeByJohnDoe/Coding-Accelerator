# Split by Moise
        
# Time = 6h (1h + 5h)
# Date = 5 & 8 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import split_index_moise

def split_exemple() :
    message_error = "error"
    
    if len(sys.argv) == 3 :

        moise = split_index_moise(sys.argv[1], sys.argv[2])
        for i in range (len(moise)) :
            print(moise[i])

    else :
        print(message_error)

split_exemple()