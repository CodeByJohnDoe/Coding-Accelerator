# Check Number
        
# Time = 40 min    
# Date = 29 aout 2023

# Import listing Char Ascii

import string 
import sys         
import numbers


if len(sys.argv)  != 2:
    check   = False
else :
    In  = str(sys.argv[1])
    check   = In.isdigit()
    
if check == True :
    if   In % 2 == 0 :
        print ("pair")
        
    elif In % 2 == 1 :
        print ("impaire")
    
else :
    print ("Tu ne me la mettra pas à l'envers")