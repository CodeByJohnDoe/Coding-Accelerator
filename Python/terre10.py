# Prime Number
        
# Time = 3 h
# Date = 1 september 2023

import sys

def check_Prime(In) :

    if In > 1 and In % 2 == 1:
        i=2
        for i in range(2,In-1) :
                
            if (In % i) == 0 :
                return False
        else :
            return True
        
    elif In == 2:
        return True
    else :
        return False  

if len(sys.argv) == 2 and sys.argv[1].isdigit() == True:
    In     = int(sys.argv[1])
        
    if check_Prime(In) == True :
        print("Oui, ",sys.argv[1]," est un nombre premier")
    else :  
        print("Non, ",sys.argv[1]," n'est pas un nombre premier")
else :
    print ("Fail type or no enough argument")    
