
# Time =  30 min


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

 