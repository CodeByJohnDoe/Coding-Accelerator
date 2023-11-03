
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

def assemble(element1, element2) :
    assembled = element1 + element2
    return(assembled)
        
def split_index_moise(to_be_compared, to_be_confronted) :
    markers = [9,11,32] # HT VT Tab ASCII
    input_split = split(to_be_compared, markers)
    space = ' '
    assembled0 = ''
    assembled1= ''
    assembled = []
    n = len(input_split)
    
    for i in range(n) :
        while input_split[i] == to_be_confronted :
            for j in range(0,i-1):
                assembled0 = assembled0 + assemble(input_split[j], space)
            for k in range(i+1,n) :
                assembled1 = assembled1 + assemble(space, input_split[k])
            assembled.append(assembled0)
            assembled.append(assembled1)
            return(assembled)

def my_concat(to_be_concat, separator) : 
    n = len(to_be_concat)
    assembled = ''
    
    for i in range (0,n) :
        assembled = assembled + assemble(to_be_concat[i], separator)
    return[assembled]

def twins(to_be_test):
    to_be_test_sorted = sorted(to_be_test)
    answer = []
    n = len(to_be_test_sorted)
    i = 0

    while i < n:
        if i == n-1 or to_be_test_sorted[i] != to_be_test_sorted[i+1]:
            answer.append(to_be_test_sorted[i])
            i += 1
        else:
            i += 2  # twins

    return answer

def one_by_one (to_be_clean):
    to_be_clean = list(to_be_clean)
    n = len(to_be_clean)
    i = 0
    
    while i < n-1:
        if to_be_clean[i] == to_be_clean[i+1]:
            del to_be_clean[i]
            n = len(to_be_clean)
            i = i
        else :
            i += 1
    clean = ''.join(to_be_clean)
    
    return clean

def add_or_subt (to_be_operated):
    
    to_be_operated_list = to_be_operated[:-1]
    to_be_applied = list(to_be_operated[-1])
    to_be_operated_list.append(to_be_applied[1])
    to_be_digit = to_be_operated_list
    is_all_digit = Is_Digit(to_be_digit)
    
    if is_all_digit == True :
        negative = "-"
        positive = "+"
        n = len(to_be_operated_list)
        result = []
        
        if to_be_applied[0] == negative :
            for i in range(n-1):
                result.append(int(to_be_operated_list[i]) - int(to_be_applied[1]))
                
        elif to_be_applied[0] == positive :
            for i in range(n-1):
                result.append(int(to_be_operated_list[i]) + int(to_be_applied[1]))
        
        return result
    
def inspection(to_be_inspected, wanted) :
    
    golem = to_be_inspected
    wanted = wanted.lower()
    g = len(to_be_inspected)
    ungolem = []

    for i in range(0,g):
        I = to_be_inspected[i]
        result_comparator = comparator_string (I.lower(), wanted)
        if result_comparator == True :
            ungolem.append(i)
    
    ungolem.reverse()
    
    for k in ungolem :
        del golem[k]
            
    return golem

def add_element_in_sort_list(sort_list, to_be_add) :
    
    if Is_Digit(sort_list) == True and Is_Digit(to_be_add):
        g = len(sort_list)
        index = 0
        new_list = []
        
        print(sort_list)
        print(g)
        
        for i in range(g):  
            if sort_list[i] <= to_be_add :
                index = i
        
        for j in range(g) :
            print(new_list)
            if j < index :
                new_list.append(sort_list[j])
            elif j == index :
                new_list.append(sort_list[j])
                new_list.append(to_be_add)
            else :
                new_list.append(sort_list[j])
        
        return new_list

    return "error"

def index_wanted (element, wanted) :
    g = len(element)
    
    for i in range (g) :
        if element[i] == wanted :
            return i

def mix_and_sorted_list (list_a, list_b) :
    new_list_sorted = []
    g_a = len(list_a)
    g_b = len(list_b)
    i = 0
    j = 0
    
    while i < g_a or j < g_b:
        if i < g_a and (j == g_b or list_a[i] < list_b[j]):
            new_list_sorted.append(list_a[i])
            i += 1
        elif j < g_b and (i == g_a or list_a[i] > list_b[j]):
            new_list_sorted.append(list_b[j])
            j += 1
        else:
            new_list_sorted.append(list_a[i])
            new_list_sorted.append(list_a[j])
            i += 1
            j += 1
           
    return new_list_sorted

def move_first_to_the_end (array):
    array_0 = array[0]
    new_array = array[1:]
    new_array.append(array_0)
    return new_array

def found_extension(filename, extension):
    if filename.endswith(extension):
        return True
    else:
        return False
    
def is_all_digit(list):
    content = []
    g = len(list)
    
    for i in range(g):
        if Is_Digit(list[i]) == True : 
            content.append(True)
        else :
            content.append(False)
    
    if all(content) == True :
        return True
    else :
        return False 
    
