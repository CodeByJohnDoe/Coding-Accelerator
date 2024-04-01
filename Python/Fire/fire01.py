# Calculator

import sys
import re # Search char

# Carch argument
def get_argument():

    # Catch command
    argument_catched = ' '.join(sys.argv[1:])
    argument_catched_len = len(sys.argv[1:]) 
        
     # Len
    expected_len_argument = 1 
    
    if argument_catched_len == expected_len_argument:
        return argument_catched
    else:
        return 'error : out range '
    
# Filter the argument    
def filter_argument(argument) :
    
    # Argument data
    argument_len = len(argument)
    argument_list = list(argument)
    
    # Init debbug
    debbug_message = []
    
    # Invalid char 
    if re.search('[^+*/()%\s\d]', argument):
        debbug_message.append('no match Char')
        return debbug_message
    else:
        debbug_message.append('match Char')
        
    # Invalid Parenthesis count       
    parentheses_left_count = int(argument.count('('))
    parentheses_right_count = int(argument.count(')'))

    if parentheses_left_count == parentheses_right_count :
        debbug_message.append('match Parenthesis count')
    else :
        debbug_message.append('no match Parenthesis count')
        return debbug_message
        
    # Invalid Positioning special char
    for i in range (0, argument_len) :
        rule = '[/*%]'
                
        if re.match(rule, argument_list[i]) != None and (argument_list[i] == argument_list[i+1]) == True:
            debbug_message.append('match Special twins char')
            return debbug_message
        
    # Remove Space
    argument_without_space = list(str(argument).replace(" ", ""))
    return argument_without_space

# The five operations
def sum (argument0, argument1) :
    result = argument0 + argument1
    return result

def sub (argument0, argument1) :
    result = argument0 - argument1
    return result

def mul (argument0, argument1) :

    result = argument0 * argument1
    return result

def div (argument0, argument1) :
    remainder = argument0
    result = [0,0]
    if argument1 == 0:
        result = None
    if remainder > argument1 :
        remainder -= argument1
        result[0] += 1
    else :
        result[1] = remainder    
    return result[0]

def mod (argument0, argument1) :
    result = div(argument0, argument1)[1]
    return result

# Call operation
def call_operation (operation, argument0, argument1):
    function_mapping = {
        '+' : sum,
        '-' : sub,
        '*' : mul,
        '/' : div,
        '%' : mod
    }
    for operation in function_mapping :
        result = function_mapping[operation](argument0, argument1)
        return result

def parenthesis_separator (argument, rule):
    n = len(argument)    
    for i in range(n) :
        while argument[i] == rule :
            del argument[i]
            result = [argument[:i],argument[i:]]
            return result

# Parenthesis priority
def parenthesis_priority (argument):
    parentheses_count = int(argument.count('('))
    while parentheses_count != 0 :
        result_left_parenthesis = parenthesis_separator(argument, '(')
        result_right_parenthesis = parenthesis_separator(result_left_parenthesis[1], ')')
        operation = [
            result_left_parenthesis[0],
            result_right_parenthesis[0],
            result_right_parenthesis[1]
        ]

# Operator priority 
def operator_priority (argument) :
    if 


# Priority manager 
def priority_manager (argument) :
    
    # Parenthesis
    parenthesis_priority(argument)
    
    # Priority operation 
    print(re.search('[*/%]', operation[1]))
        
    
    # Simple operation
    
    
    return result

# The main function        
def calculator () : 
    print(filter_argument(get_argument()))
    result = priority_manager(filter_argument(get_argument()))
    return result
        
calculator()