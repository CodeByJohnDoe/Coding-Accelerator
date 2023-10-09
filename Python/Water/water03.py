# Fibonacci sequence
        
# Time = 3h30
# Date = 26 & 30 september 2023
# Don't really understant the instructions, 2h30 in trash 


import sys

def Sequence_Fibonacci() :
    error_arg = -1
    
    if len(sys.argv) == 2 :
                
        START_FIBONACCI = 0
        FIRST_FIBONACCI = 1
        
        target_fibonacci = str(sys.argv[1])
        is_digit_target_fibonacci = target_fibonacci.isdigit()
        
        if is_digit_target_fibonacci == True and int(target_fibonacci) > 0:
            list_fibonacci = [START_FIBONACCI, FIRST_FIBONACCI]
            target_fibonacci = int(target_fibonacci)+1          
            i = len(list_fibonacci)-1     
            
            while i < target_fibonacci :
                print(list_fibonacci)
                list_fibonacci.append(list_fibonacci[-1]+list_fibonacci[-2])
                i += 1
            print(list_fibonacci[-1])
        else :
            print(error_arg)
    else :
        print(error_arg)
        
Sequence_Fibonacci()