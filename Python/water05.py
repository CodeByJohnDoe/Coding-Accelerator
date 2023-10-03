# Comparator String
        
# Time = 3h + 10 min to export
# Date = 30 september 2023

import sys

def Comparator_String(to_be_compared, to_be_confronted) :
    error_arg = "error"
    error_not_found = "False"
    
    #if len(sys.argv) == 3 :
    to_be_compared = list(str(to_be_compared))   #    to_be_compared = list(str(sys.argv[1]))
    to_be_confronted = list(str(to_be_confronted)) #    to_be_confronted = list(str(sys.argv[2]))
    to_be_compared_len = len(to_be_compared)
    to_be_confronted_len = len(to_be_confronted)
    comparator = []
    i = len(comparator) 

    if to_be_compared_len >= to_be_confronted_len and comparator != to_be_confronted and len(comparator) >= i:

        while i != len(to_be_compared) and to_be_confronted_len > i:
            
            if to_be_compared[i] == to_be_confronted[i] :
                comparator.append(to_be_confronted[i])
                i += 1    

            else :
                if i == 0 :
                    i += 1 
                    
                to_be_compared = to_be_compared[i:]
                comparator = []
                i = 0
                
    if comparator == to_be_confronted :
        return("True") # print
                                
    else :
            return(error_not_found) #print
            
    #else :
    #    exit(error_arg)
        
# Comparator_String(sys.argv[1], sys.argv[2])