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

def Check_Sort() :
            
    List = []
    
    for i in range (1, len(sys.argv)) :
        List.append(sys.argv[i])
    
    for i in range(1, len(List)): 
   
            a = List[i] 
   
            j = i - 1 
           
            while j >= 0 and a < List[j]: 
                List[j + 1] = List[j] 
                j -= 1 
                 
            List[j + 1] = a 
    
    return List

if len(sys.argv) == 4 and Check_Digit() == True:

    if Check_Egal() == True: 
        Out = Check_Sort()[round((len(sys.argv))/2)-1]
        print(Out)
        
    else:
        print('erreur.')
        
else:
    print('erreur.')