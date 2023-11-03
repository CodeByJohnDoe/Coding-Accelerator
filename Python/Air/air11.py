# pyramid
        
# Time = 30 min 
# Date = 3 novembre 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import Is_Digit

def pyramid_exemple() :
    message_error = "error"
    g = len(sys.argv)
    
    if g == 3 and len(sys.argv[1]) == 1:
        level_is_digit = Is_Digit(sys.argv[2])
        level_max = int(sys.argv[2])

        if level_is_digit == True and level_max > 0:
            char = sys.argv[1]
            g = level_max * 2 +1
            content = [' '] * g
                    
            for i in range(level_max) :          
                content[level_max-i] = char
                content[level_max+i] = char
                print(''.join(content))
        else :
            print(message_error)
            
    else :
        print(message_error)

pyramid_exemple()