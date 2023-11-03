# Add a number to a sort list
        
# Time = 45 min
# Date = 27 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import add_element_in_sort_list

def add_number_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 4 :
        sort_list  = sys.argv[1:-1]
        to_be_add = sys.argv[-1]
        new_sort_list = add_element_in_sort_list (sort_list, to_be_add)
        print(' '.join(map(str,new_sort_list)))


    else :
        print(message_error)

add_number_exemple()