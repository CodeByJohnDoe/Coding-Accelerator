# Square root 
        
# Time = 2 h
# Date = 31 aout 2023

import sys
import math

Len         = len(sys.argv)
Check       = sys.argv[1].isdigit()


if len(sys.argv) == 2 and Check == True:
    
    Num1        = sys.argv[1].isnumeric()    
    Argv1       = int(sys.argv[1])

    if int(Num1) > 0 :
        
        Out     = math.pow(Argv1, 0.5)   
        print(int(Out))

    else :
        print('erreur. The digit must me upper thant 0')

else :
    print("erreur. only digit")

    
