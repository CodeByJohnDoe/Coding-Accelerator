#Sort ASCII
        
# Time = 1h 
# Date = 4 october 2023

import sys
from unbuilt_function import Is_Letter, Select_Sort

def ASCII_Sort() :
    message_error = "error"
    is_all_letter = []
    s = len(sys.argv)
    
    for i in range (1,s) :
        is_all_letter.append(Is_Letter(sys.argv[i]))
   
    if all(is_all_letter) == True and s > 2:
        list_unsort = []    
        
        for h in range (1, s) :
            list_unsort.append(sys.argv[h])      
            
        print(Select_Sort(list_unsort))       
            
    else :
        print(message_error)
    
ASCII_Sort()