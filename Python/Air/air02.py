# Concat
        
# Time = 10 min
# Date = 8 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import my_concat

def concat_exemple() :
    message_error = "error"
    to_be_concat = []
    separator = sys.argv[-1]
    n = len(sys.argv)
    
    if len(sys.argv) >= 3 :
        
        for i in range (1,n-1) :
            to_be_concat.append(sys.argv[i])

        my_concat_result = my_concat(to_be_concat, separator)
        print(my_concat_result[0])

    else :
        print(message_error)

concat_exemple()