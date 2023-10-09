# Switzerland
        
# Time = 3 h
# Date = 2 september 2023

import sys

def Check_Digit() :
    
    List = []
    
    for i in range(1,len(sys.argv)) :
        
        List.append(sys.argv[i].isdigit())
            
    if all(List) == True :        
        return True
    
    elif all(List) == False :
        return False

def Check_Egal() :
    
    List = []
    
    for i in range (1,len(sys.argv)) :
        
        for j in range (2,len(sys.argv)) :
            
            if i == j :
                +j
                              
            elif sys.argv[i] == sys.argv[j] :  
                
                List.append(False)
                
            else :
                List.append(True)
    
    if all(List) == True :        
        return True
    
    else:
        return False
