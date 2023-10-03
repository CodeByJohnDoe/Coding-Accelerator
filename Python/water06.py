# Capital letters 1/2
        
# Time = 1h45
# Date = 30 september 2023
# 

import sys



def Has_Numbers(input_string):
    return any(char.isdigit() for char in input_string)

def Capital_Letter_Step2() :
    a = 97
    z = 122
    A = 65
    Z = 90
    gap_a_A = a - A
    
    if len(sys.argv) == 2 :
        to_be_change = list(str(sys.argv[1]))

        len_argv1 = len(to_be_change)
        i = 0
        j = 0
        l = 2

        to_be_send = []
        
        if Has_Numbers(sys.argv[1]) == False :

            while i in range (len_argv1) :
                x = ord(to_be_change[i])
                to_be_lower = to_be_change
                
                if x >= A and x <= Z :
                    to_be_lower[i] = chr(x + gap_a_A)
                
                i += 1
                       
            while j in range (len_argv1) :
                x = ord(to_be_lower[j])
                
                if x >= a and x <= z :
                    if l % 2 == 0 :
                        to_be_send.append(chr(x - gap_a_A))
                        l += 1
                    else :
                        to_be_send.append(chr(x))
                        l += 1

                else :
                    to_be_send.append(to_be_change[j])
                    
                j += 1
                
            print(''.join(to_be_send))
        else :
            quit("error")
                
    else :
        quit("error")
        
Capital_Letter_Step2()