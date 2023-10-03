# Min Max
        
# Time = 1h
# Date = 2 october 2023
# Import water 8

import sys
from water08 import Check_Digit

def Min_Max() :

    message_error = "error"

    if len(sys.argv) == 3 :
        
        argv1 = 1
        argv2 = 2
        is_digit_argv1 = Check_Digit(argv1)
        is_digit_argv2 = Check_Digit(argv2)  
            
        
        if is_digit_argv1 == True and is_digit_argv2 == True :
            
            list_input = [int(sys.argv[1]), int(sys.argv[2])]
            list_input.sort()
            list_sort = list_input
            list_delta = list_sort[1] - list_sort[0] - 1
            to_be_send = [list_sort[0]]
            i = 0

            if list_delta > 0 :
                
                for i in range(list_delta) :
                    to_be_send.append(to_be_send[-1] + 1)
                    i += 1
                
                print(' '.join(map(str, to_be_send)))
            
            else :
                exit(message_error)
        
        else :
            exit(message_error)
    
    else :
        exit(message_error)

Min_Max()