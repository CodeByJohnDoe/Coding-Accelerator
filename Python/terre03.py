# Alphabet Start     
        
# Time = 20 min    
# Date = 29 aout 2023

# Import listing Char Ascii

import string 
import sys         

a   = 97
z    = 123
Out     = ""

start = ord(sys.argv[1])

for i in range (start,z) :
        Out = Out + chr(i)
    
print("Exercice : ", Out)
