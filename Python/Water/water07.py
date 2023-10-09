# Capital letters first
        
# Time = 40 min
# Date = 1 ocotbre
# 

import sys



def Has_Numbers(input_string):
    return any(char.isdigit() for char in input_string)

def Capital_Letter_First_Letters() :
    a = 97
    z = 122
    A = 65
    Z = 90
    gap_a_A = a - A
    markers = [9,11,32] # HT VT Tab ASCII
    
    if len(sys.argv) == 2 :
        to_be_change = list(str(sys.argv[1]))

        len_argv1 = len(to_be_change)
        i = 0
        j = 0
        l = 1

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
                
                if l == 1 and x >= a and x <= z :
                    to_be_send.append(chr(x - gap_a_A))
                    l = 0
                    
                elif l == 0 and x >= a and x <= z :
                    to_be_send.append(chr(x))
                    
                elif l == 0 and x in markers :
                    to_be_send.append(to_be_change[j])
                    l = 1       
                    
                else :
                    to_be_send.append(to_be_change[j])
                    
                j += 1
                
            print(''.join(to_be_send))
            
        else :
            quit("error")
                
    else :
        quit("error")
        
Capital_Letter_First_Letters()