# Twins
        
# Time = 1h20
# Date = 10 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import twins

def twins_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 3 :
        to_be_test =[]
        to_be_test  = sys.argv[1:]
        print(to_be_test)
        answer_twins = twins (to_be_test)
        print(answer_twins[0])

    else :
        print(message_error)

twins_exemple()