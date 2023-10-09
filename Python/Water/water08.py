# Only Number
        
# Time = 10 min + 1h (water09)
# Date = 1 octobre
# Import Terre13 Check_Digit()

import sys

def Is_Digit(argv) :
    
    List = []
    list_input_argv = argv
    
    for i in range(0,len(list_input_argv)) :
        
        List.append(str(list_input_argv[i]).isdigit())
            
    if all(List) == True :        
        return True
    
    elif all(List) == False :
        print(List)
        return False


def Check_Digit_Argv(num_argv) :
    if len(sys.argv) == num_argv + 1: # return = print
        
        if len(sys.argv[num_argv]) == 0 :
            return("False") 
        else :
            return(Is_Digit(sys.argv[num_argv]))
#    else :
#        exit("error")
    
Check_Digit_Argv(1)