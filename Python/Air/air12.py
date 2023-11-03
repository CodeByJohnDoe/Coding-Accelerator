# King of sort
        
# Time = 10 min (Already done )
# Date = 3 novembre 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import is_all_digit, Select_Sort

def king_of_sort_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 3:
        content = sys.argv[1:]
        
        all_digit = is_all_digit(content)
        
        if all_digit == True :
            print(Select_Sort(content))
        
        else :
            print(message_error)
            
    else :
        print(message_error)

king_of_sort_exemple()