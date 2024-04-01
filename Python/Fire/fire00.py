# Show rectangle

# Trop de parametre et éviter de répeter path ce genre de chose 1 -3 param max

import sys

def validate_input():

    debbug_message = []
    input_string_list = sys.argv[1:]

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

    if validate_input () is None :
        
        # Init patern char
        char_corner = 'o'
        char_width  = '-'
        char_height = "|"
        char_empty = ' '
        
        # Catch wight and height
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        
        first_line = ''
        seconde_line = ''
        
        if width >= 1 and height >= 1 :
            
            # Width traitement
            if width == 1 :
                first_line = char_corner
            elif width == 2 :
                first_line = char_corner + char_corner
            else :
                first_line = char_corner + (char_width * (width - 2)) + char_corner
                                
            # Height traitement
            if height ==1 :
                print(first_line)
            elif height == 2 :
                print(first_line)
                print(first_line)
            else :
                print(first_line)
                for i in range(0, height-2) :
                    seconde_line = char_height + char_empty * (width - 2) + char_height
                    print(seconde_line)
                print(first_line)
                                          
        print()
            
    else :
        return message_error

make_my_rectangle()