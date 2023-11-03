# blend & sorted by fusion
        
# Time = 1h 30
# Date = 27 october 2023

import sys
sys.path.append("/home/uf/Desktop/Coding Accelerator/Python")
from unbuilt_function import index_wanted, mix_and_sorted_list, Is_Digit

def blender_sorted_exemple() :
    message_error = "error"
    
    if len(sys.argv) >= 4 :
        argv = sys.argv[1:]
        wanted = "fusion"
        index = index_wanted(argv, wanted)
        list_a = sys.argv[1:index]
        list_b = sys.argv[index+2:]

        if Is_Digit(list_a) == True and Is_Digit(list_b) == True :

            new_sort_list = mix_and_sorted_list (list_a, list_b)
            print(' '.join(map(str,new_sort_list)))
            
        else :
            print(message_error)

    else :
        print(message_error)

blender_sorted_exemple()    