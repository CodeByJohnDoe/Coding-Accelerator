# Absolute min difference
        
# Time algo = 2h 30
# Date = 3 october 2023

import sys
from unbuilt_function import Is_Digit, Exclude

def Absolute_Min_Difference() :
    message_error = "error"

    value_imput = []
    exclude_list_ascii = [45]
  
    for i in range(1, len(sys.argv)) :
        value_imput.append(Exclude(sys.argv[i], exclude_list_ascii))
        i += 1  
        
    is_all_digit = []

    for j in range (0,len(value_imput)) :
        is_all_digit.append(Is_Digit(str(value_imput[j])))
        j += 1

    if all(is_all_digit) == True and len(sys.argv) > 2 :
        value_will_be_sort = []

        for k in range (0,len(value_imput)) :
            value_will_be_sort.append(int(value_imput[k]))
            k += 1
         
        value_sort = sorted(value_will_be_sort)
        result = value_sort[1] - value_sort[0]

        for l in range (1, len(value_sort)-1) :
            result_k = value_sort[l+1] - value_sort[l]
            
            if result > result_k :
                result = result_k           
            l += 1
            
        print(result)
        
    else :
        print(message_error)    
    
Absolute_Min_Difference()