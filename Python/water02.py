# Argv wrong way
        
# Time = 10 min
# Date = 26 september 2023

import sys

len_argv = len(sys.argv)

def Reverse_ARGV ():

    if len_argv > 1 :
        for i in range (1, len_argv) :
            print(sys.argv[len_argv-i])
    else : 
        print('error')

Reverse_ARGV()