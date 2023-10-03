# Only Number
        
# Time = 10 min + 1h
# Date = 1 octobre
# Import Terre13 Check_Digit()

import sys

def Check_Digit(num_argv) :
    
    List = []
    
    for num_argv in range(1,len(sys.argv)) :
        
        List.append(sys.argv[num_argv].isdigit())
            
    if all(List) == True :        
        return True
    
    elif all(List) == False :
        return False


def Check_Digit_Argv(num_argv) :
    if len(sys.argv) == num_argv + 1: # return = print
        
        if len(sys.argv[num_argv]) == 0 :
            return("False") 
        else :
            return(Check_Digit(num_argv))
#    else :
        exit("error")
    
Check_Digit_Argv(1)