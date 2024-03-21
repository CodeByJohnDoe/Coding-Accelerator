# Unit test
        
# Time = 0.5h + 9h
# Date = 22 novembre 2023 + 9 Février 2024

import sys
import os
import json
import subprocess
from colorama import Fore, Back, Style


path = "/home/uf/Desktop/Coding Accelerator/Python"
sys.path.append(path)
from unbuilt_function import *

## Tools box 

def tool_box():

    debbug_message = []
    input_string_list = sys.argv[1:]

    ## Arguments

    # Len 
    input_string_len = len(input_string_list)
    
    if input_string_len == 0:
        debbug_message.append('match Len')
    else:
        debbug_message.append('no match Len')
        return debbug_message
    
    # Number and letter checks
    check_list_number = []
    check_list_letter = []
    
    for i in range(0, input_string_len):
        check_list_number.append(str(input_string_list[i]).isdigit())
            
        if all(check_list_number):
            debbug_message.append('match all Number')
            check_list_letter.append(str(input_string_list[i]).isdigit())
                
        if all(check_list_letter):        
            debbug_message.append('match all Letter')
        
        elif not all(check_list_letter):
            debbug_message.append('no match all Letter')
            return debbug_message

    # Found file length / Name
    check_list_files_names = os.listdir(path)
    len_list_files_names = len(check_list_files_names) 
    
    if len_list_files_names == 8:
        debbug_message.append('match Length')

    else:
        debbug_message.append('no match Length')
        return debbug_message
  
    if check_list_files_names[0] == 'Air':
        debbug_message.append('match Name')

    else:
        debbug_message.append('no match Name')
        return debbug_message
        
def load_json() :
        
    # Import json    
    path = "/home/uf/Desktop/Coding Accelerator/Python/Air"
    sys.path.append(path)
    
    # Open json data
    try:
        with open(os.path.join(path, 'air13.json'), 'r') as data:
            data_json = json.load(data)
                    
        return data_json
        
    except FileNotFoundError:
        return("'air13.json' No found")

## The unit test

def unit_test() :
    
    if tool_box() is None:

        data_json = load_json()
          
        # Text color
        COLOR_SUCCESS = Fore.GREEN
        COLOR_FAILURE = Fore.RED
        COLOR_RESULT = Fore.YELLOW
        RESET_COLOR = Style.RESET_ALL
        
        # Listing files
        path = "/home/uf/Desktop/Coding Accelerator/Python/Air"
        
        # Initialize counters                       
        pass_test_counter = 0
        total_test_counter = 0  
                
        # Extracting data for current test
        for json_obj in data_json:
            sub_test_counter = 0  
            sub_pass_test_counter = 0
            
            # Extracting data for current test
            current_data_name = json_obj.get("name", "")
            script_path = os.path.join(path, current_data_name)     
            
            number_of_test = len(json_obj.get('input', []))
            
            for i in range (number_of_test) :  
                current_data_input = json_obj.get('input', [])[i]
                current_data_target = json_obj.get('expected_output', [])[i]     
                
                # Start the script process and send input data one by one
                args = ['/usr/bin/python3', script_path] + current_data_input
                process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                # Read the output from the process
                stdout, stderr = process.communicate()
                
                compare_data_target =[]
                compare_data_target.append(stdout)
                
                # Update counters and see result
                if current_data_target == compare_data_target :
                    pass_test_counter += 1
                    sub_pass_test_counter += 1
                    print(f"{COLOR_SUCCESS}{current_data_name}({sub_pass_test_counter}/{number_of_test}): success{RESET_COLOR}")

                else :
                    print(f"{COLOR_FAILURE}{current_data_name}({sub_pass_test_counter}/{number_of_test}): failure {RESET_COLOR}")
                    
                total_test_counter+= 1
                sub_test_counter += 1

        print(f"{COLOR_RESULT}Total success: ({pass_test_counter}/{total_test_counter}){RESET_COLOR}")

unit_test()