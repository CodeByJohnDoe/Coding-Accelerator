# Fibonacci sequence
        
# Time = 30min
# Date = 30 september 2023
# Terre10 Prime Number import Check_Prime


import sys

def Check_Prime(In) :

    if In > 1 and In % 2 == 1:

        for i in range(2,In-1) :
                
            if (In % i) == 0 :
                return False
        else :
            return True
        
    elif In == 2:
        return True
    else :
        return False  


def Sequence_Prime_Number() :
    error_arg = -1
    
    if len(sys.argv) == 2 :
        start_prime = str(sys.argv[1])
        is_digit_start_prime = start_prime.isdigit()

        if is_digit_start_prime == True and int(start_prime) > 0:  
            answer_check_prime = False
            start_prime = int(start_prime)
            test_number_prime = start_prime
            
            while answer_check_prime != True :
                test_number_prime += 1
                answer_check_prime = Check_Prime(test_number_prime)
            print(test_number_prime)
        else :
            print(error_arg)
    else :
        print(error_arg)
        
Sequence_Prime_Number()