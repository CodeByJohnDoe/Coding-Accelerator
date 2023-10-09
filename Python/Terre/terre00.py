# Alphabet          
        
# Time = 30 min    
# Date = 29 aout 2023

# Import listing Char Ascii

import string           
           
# Solution

Out = string.ascii_lowercase

print("Solution : ", Out)


# Without Ascii_lowercase

a   = 97
z   = 123 
Out = ""

for i in range (a,z) :
    Out = Out + chr(i)

print("Exercice : ", Out)
