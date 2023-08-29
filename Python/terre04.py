# Check Number
        
# Time = 30 min    
# Date = 29 aout 2023

# Import listing Char Ascii

import string 
import sys         

check   = isinstance(int(sys.argv[1]), int)

if check == True :
    In      = int(sys.argv[1])
    if   In % 2 == 0 :
        print ("pair")
        
    elif In % 2 == 1 :
        print ("impaire")
        
else :
    print ("Tu ne me la mettra pas à l'envers")