
# If export lib, change name def to lowercase

import sys

def Is_Digit(argv) :
    
    List = []
    list_input_argv = argv
    
    for i in range(0,len(list_input_argv)) :
        
        List.append(str(list_input_argv[i]).isdigit())
            
    if all(List) == True :        
        return True
    
    elif all(List) == False :
        return False

def Is_Letter(argv) :
    
    List = []
    list_input_argv = argv
    
    for i in range(0,len(list_input_argv)) :
        
        List.append(str(list_input_argv[i]).isalpha())
            
    if all(List) == True :        
        return True
    
    elif all(List) == False :
        return False

def Exclude (string_in, exclude_list_ascii) : 
    list_string_in = list(string_in)
    list_string_out = []
               
    for i in range (len(list_string_in)) :
        
        if ord(list_string_in[i]) in exclude_list_ascii :
            i += 1
            
        else :
            list_string_out.append(list_string_in[i])
            i += 1
            
    string_out = ''.join(map(str,list_string_out))
    return string_out
    
def Is_Sorted(list) :
    list_out = []
    
    for i in range(1, len(list)): 
        a = list[i] 
        j = i - 1 
        
        if list[j] < list[i]:
            list_out.append(True)  
        else :
            list_out.append(False)               
                    
    if all(list_out) == True :        
        return True
    
    else:
        return False
    
def Bubble_Sort(list) :
    
    n = len(list)
    
    for j in range(n) :
        for k in range(0, n-j-1) :
            if list[k] > list[k+1] :
                list[k], list[k+1] = list[k+1], list[k]
    return(' '.join(list))

def Select_Sort(list) :
    
    n = len(list)
    
    for j in range(n) : 
        min = j
        
        for k in range(j+1, n) :
            
            if list[k] < list[min] :
                min = k
            
        if min != j :
            list[j], list[min] = list[min], list[j]
            
    return(' '.join(list))   

def split(argv, rule_to_split_in_ascii) :
    n = len(argv)
    list_input = list(argv)
    list_input.append(" ") # Extend i range
    list_input.append('.') # Extend i range
    split = []
    split_cursor = 0
    split_tempo = '' 
    split_output = []
    
    for i in range(0,n+1) :

        while ord(list_input[i]) in rule_to_split_in_ascii :
            split = []                   
            
            for j in range(split_cursor, i) :
                split.append(list_input[j])
                j += 1
                
            split_cursor = i+1
            
            if split_cursor != n :
                split_output.append(''.join(split))
                split = []
                
            i += 1
            
    return split_output

# Dependence = index()
def comparator_string(to_be_compared, to_be_confronted) :
    error_not_found = False
    
    to_be_compared = list(str(to_be_compared))   
    to_be_confronted = list(str(to_be_confronted))
    to_be_compared_len = len(to_be_compared)
    to_be_confronted_len = len(to_be_confronted)
    comparator = []
    i = len(comparator) 

    if to_be_compared_len >= to_be_confronted_len and comparator != to_be_confronted and len(comparator) >= i:

        while i != len(to_be_compared) and to_be_confronted_len > i:
            
            if to_be_compared[i] == to_be_confronted[i] :
                comparator.append(to_be_confronted[i])
                i += 1    

            else :
                if i == 0 :
                    i += 1 
                    
                to_be_compared = to_be_compared[i:]
                comparator = []
                i = 0
                
    if comparator == to_be_confronted :
        return(True)
                                
    else :
        return(error_not_found)

def index(to_be_compared, to_be_confronted) :
    for i in range (len(to_be_compared)) :

    
        if to_be_compared[i] == to_be_confronted : 
            return i
    return -1

#def split_moise(to_be_compared, to_be_confronted) :
    
