# different number sequences
        
# Time = 2h + 1h
# Date = 23 & 26 september 2023


def sequence():    
    
    list_number = []
    
    for i in range (10) :
        for j in range (10) :
            for k in range (10) :
                if i < j < k and i != j != k :
 
                    list_number.append(f"{i}{j}{k}")
                    
    print (', '.join(map(str, list_number)))
    
sequence()