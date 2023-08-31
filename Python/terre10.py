# Prime Number
        
# Time = 1 h
# Date = 31 aout 2023

import sys

In        = list(sys.argv[1])
List      = []
Size      = len(In)

for i in range (Size) :
    List.insert(0,In[i])

print("Reverse  of ",sys.argv[1],' : ' ,''.join(List))



print("Oui, ",sys.argv[1]," est un nombre premier")
print("Non, ",sys.argv[1]," est un nombre premier")