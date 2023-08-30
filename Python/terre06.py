# Reverse string
        
# Time = 4 h
# Date = 30 aout 2023

import sys

In        = list(sys.argv[1])
List      = []
Size      = len(In)

for i in range (Size) :
    List.insert(0,In[i])

print("Reverse  of ",sys.argv[1],' : ' ,''.join(List))
