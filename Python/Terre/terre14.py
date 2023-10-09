# Sort or Not 
        
# Date = 11 spetember 2023 arrêet pour caause de finance 
# Reprise le 23 september 2023  time = 1h

import sys

def Check_Digit() :
    
    List = []
    
    for i in range(1,len(sys.argv)) :
        
        List.append(sys.argv[i].isdigit())
            
    if all(List) == True :        
        return True
    
    elif all(List) == False :
        return False


def Check_Sort() :
            
    List = []
    
    for i in range (1, len(sys.argv)) :
        List.append(sys.argv[i])
 
    for i in range(1, len(List)): 
   
            a = List[i] 
   
            j = i - 1 
            
            if List[j] < List[i]:
                List.append(True)  
            else :
                List.append(False)                
                
                    
    if all(List) == True :        
        return True
    
    else:
        return False


if Check_Digit() == True and len(sys.argv) > 1:

    if Check_Sort() == True:
        print('Triée !')        
        
    elif Check_Digit() == True:
        print('Pas triée !')

else:
    print('erreur.') 