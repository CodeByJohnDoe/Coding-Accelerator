# Power of Number
        
# Time = 2 h
# Date = 31 aout 2023

import sys

Len     = len(sys.argv)

if len(sys.argv) == 3 :
    
    Num1        = sys.argv[1].isnumeric()
    Num2        = sys.argv[2].isnumeric()
    
    Argv1       = int(sys.argv[1])
    Argv2       = int(sys.argv[2])

    if int(Num2) > 0 :
    
        if Num1 == True and Num2 == True:
        
            Out     = ''
            i       = 0
                
            for i in range(Argv2-1) :
                
                if i == 0 :
                    Out = Argv1*Argv1
                else :
                    Out = Out * Argv1 
                
            print(Out)
                                
        else :
            print('erreur.3')

    
    else :
        print('erreur.2')

else :
    print("erreur.1")

    
