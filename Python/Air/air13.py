# Unit test
        
# Time = 0.5h + 9h
# Date = 22 novembre 2023 + 9 Février 2024

import sys
import os
import json
import subprocess
import glob

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
    
    if len_list_files_names == 6:
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

        # Arrange data from json
        name_data_json = list(data_json.keys())
        len_datajson = len(data_json) -1
        
        # Listing files
        list_files_names = glob.glob(path + '/*')

        # 
        with open(os.path.join(path, name_data_json[0],"r")) as f: 
            print(f.read())

        




        # Initialize counters                       
        pass_test_counter = 0
        test_counter_done = 0                  

        number_of_test = len(data_json.get(name_data_json[0], []))
        print(number_of_test)
                    
        for test_name, tests_list in data_json.items():
            
            # Process each test in the list
            for test in tests_list:
                
                # Extract details of the test
                details_test = (test[test_name])
                
                # Send test
                input_test = details_test["input"]  # Get input for the test
                
                # Catch result
                result = subprocess.run(["python", ] + input_test, capture_output=True, check=True)

unit_test()