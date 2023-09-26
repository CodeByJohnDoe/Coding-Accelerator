# different number sequences
        
# Time = 16h01 - 
# Date = 23 september 2023

import sys

List_out = []

# F S T Ag Afs Aft Ast

List_number = list(range(10))

Dict_temp = {}

for f in range (10) :
    
    Dict_temp["F"] = f
    
    List_number_s = List_number
    List_number_s.remove(f)    
    
    for s in range (1, List_number_s) :
        

        
        Dict_temp["S"] = s
        
        List_number_t = List_number_s
        List_number_t.remove(s)       
         
        for t in range (10) :
            

            Dict_temp["T"] = t
            
            
            List_out.append(Dict_temp)
            

    
print(List_out)



# print("list without key only value dict")