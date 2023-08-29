# Division
        
# Time = 10 min    
# Date = 29 aout 2023

import sys
import math


dividend   = int(sys.argv[1])
divider    = int(sys.argv[2])

print(dividend)
print(divider)

if divider == 0 or dividend < divider: 
    print ("erreur")
else :
    
    result = math.floor(dividend / divider)
    rest   = dividend - (result * divider)

    print ("résultat : ", result)
    print ("reste    : ", rest) 