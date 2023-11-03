# Found Golem
        
# Time = 1h + 3h + 1 h
# Date = 10 & 17 & 27 october 2023

# weird instructions

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import inspection

def inspection_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 3 :
        to_be_inspected  = sys.argv[1:-1]
        wanted = sys.argv[-1]
        golem = inspection (to_be_inspected, wanted)
        g = len(golem)
        
        if g > 1 :
            print(', '.join(map(str,golem)))
        else :
            print(golem[0])

    else :
        print(message_error)

inspection_exemple()