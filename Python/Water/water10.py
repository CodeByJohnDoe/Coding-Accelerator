# Index wanted
        
# Time algo = 20 min + 10 min
# Time import match = 1h
# Date = 2 october 2023
# Water05

import sys
from water05 import Comparator_String

def Index_Wanted() :

    message_error = "error"
    start_argv = 1


    if len(sys.argv) > 2 :
       to_be_confronted = sys.argv[-1]
       solution = -1
       to_be_compared = []  
        
       for i in range (start_argv, len(sys.argv)-1) :

            to_be_compared.append(sys.argv[i])
            result_comparator = Comparator_String(to_be_compared[-1], to_be_confronted)
       
            if result_comparator == True : 
                solution = len(to_be_compared)
                print(solution)
            i += 1

    else :
        exit(message_error)

Index_Wanted()