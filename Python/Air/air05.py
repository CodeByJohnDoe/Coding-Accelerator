# Add or Subt with the last
        
# Time = 1h (I don't i take a nap :p)
# Date = 10 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import add_or_subt

def add_or_subt_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 3 :
        to_be_operated  = sys.argv[1:]
        print(to_be_operated)
        result = add_or_subt (to_be_operated)
        print(' '.join(map(str,result)))

    else :
        print(message_error)

add_or_subt_exemple()