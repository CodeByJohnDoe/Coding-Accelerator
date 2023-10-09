# Split by Moise
        
# Time 1h nul
# Date = 5 & 8 october 2023

import sys
sys.path.append("Python/unbuilt_function.py")
from unbuilt_function import index

def split_exemple() :
    message_error = "error"
    
    if len(sys.argv) == 3 :

        moise_index = index(sys.argv[1], sys.argv[2])
        print(moise_index)

        
    else :
        print(message_error)

split_exemple()