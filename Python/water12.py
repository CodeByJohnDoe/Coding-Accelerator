# Bubble Sort
        
# Time algo = 2h + 30 min
# Date = 3 & 4 october 2023

import sys
from unbuilt_function import Is_Digit, Bubble_Sort

def Bublle_Sort() :
    message_error = "error"
    is_all_digit = []
    
    for i in range (1,len(sys.argv)) :
        is_all_digit.append(Is_Digit(sys.argv[i]))
   
    if all(is_all_digit) == True and len(sys.argv) > 2:
        list_number = []    
        
        for h in range (1, len(sys.argv)) :
            list_number.append(sys.argv[h])
        
        print(Bubble_Sort(list_number))

    else :
        print(message_error)
    
Bublle_Sort()