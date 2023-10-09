# Twins
        
# Time = 10 min
# Date = 8 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import my_concat

def twins_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 3 :

        my_concat_result = my_concat()
        print(my_concat_result[0])

    else :
        print(message_error)

twins_exemple()