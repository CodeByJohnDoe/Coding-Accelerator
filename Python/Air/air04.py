# One by One
        
# Time = 45 min
# Date = 10 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import one_by_one

def one_by_one_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 2 :
        to_be_clear  = sys.argv[1]
        answer_one_by_one = one_by_one (to_be_clear)
        print(answer_one_by_one)

    else :
        print(message_error)

one_by_one_exemple()