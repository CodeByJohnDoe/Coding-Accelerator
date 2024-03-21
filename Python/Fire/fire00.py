# Show rectangle

import sys
import os

path = "/home/uf/Desktop/Coding Accelerator/Python"
sys.path.append(path)

def tool_box():

    debbug_message = []
    input_string_list = sys.argv[1:]

    ## Arguments

    # Len 
    input_string_len = len(input_string_list)
    
    if input_string_len == 2:
        debbug_message.append('match Len')
    else:
        debbug_message.append('no match Len')
        return debbug_message
    
    # Number 
    check_list_number = []
    check_list_letter = []
    
    for i in range(0, input_string_len):
        check_list_number.append(str(input_string_list[i]).isdigit())
            
        if all(check_list_number):
            debbug_message.append('match all Number')
            check_list_letter.append(str(input_string_list[i]).isdigit())
                

def make_my_rectangle () :
    message_error = "error"

    if tool_box () is None :
        char_corner = 'o'
        char_width  = '-'
        char_height = "|"
        
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        
        my_rectangle = []
        
        if width >= 1 and height >= 1 :
            if width ==1 :
                my_rectangle.append(char_corner)
                
            elif width == 2 :
                my_rectangle.append(char_corner)
                my_rectangle.insert(0,char_corner)
            else :
                print("e")
                
        print(join(my_rectangle))
        
    
    else :
        return message_error

make_my_rectangle()