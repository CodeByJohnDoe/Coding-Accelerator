# move first to the end
        
# Time = 8 min
# Date = 30 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import move_first_to_the_end

def move_first_to_the_end_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 3 :
        argv = sys.argv[1:]

        new_array = move_first_to_the_end (argv)
        print(', '.join(map(str,new_array)))

    else :
        print(message_error)

move_first_to_the_end_exemple()    