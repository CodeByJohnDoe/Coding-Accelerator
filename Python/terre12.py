# Format Hours 12 to 24
        
# Time = 2h
# Date = 1 september 2023

import sys
import re

Erreur      = 'erreur, please enter yours time like that HH:mmPM or HH:mmAM with HH < 13 and mm < 61'

def check_format() :
    
    
    Check       = re.search(':' ,sys.argv[1])

    Check_AM    = re.search('AM',sys.argv[1])
    Check_PM    = re.search('PM',sys.argv[1])
    
    if Check != None and (Check_AM != None or Check_PM != None) :
        
        L0      = False
        L1      = False
        
        List    = sys.argv[1].split(":")
        List_1  = re.sub("\D","", List[1])

        if len(sys.argv) == 2 :
            L0  = List[0].isdigit()
            L1  = List_1.isdigit()
            
        if L0 == True and L1 == True and int(List[0]) < 13 and int(List_1) < 61 and len(List[0]) == 2 and len(List_1) == 2:
            return True
        
        else :
            print(Erreur)
            
    else :
        print(Erreur)
    return False

        
if len(sys.argv) == 2 and check_format() == True :
    
        
    Check_AM    = re.search('AM',sys.argv[1])
    Check_PM    = re.search('PM',sys.argv[1])    
    List    = sys.argv[1].split(":")
    List_1  = re.sub("\D","", List[1])
    Mod     = [0,List_1]
    Out     = ''

    if  Check_AM != None and int(List[0]) == 12 :
        Mod[0] = 0  
        
    elif Check_AM != None :
        Mod[0] = List[0]
        
    elif Check_AM != None and int(List[0]) == 12 :
        Mod[0] = 12      
    
    elif Check_PM != None and int(List[0]) == 12 :
        Mod[0] = 12      
        
    elif Check_PM != None:
        Mod[0] = int(List[0]) + 12
    
    print(Mod[0], end=':') 
    print(Mod[1])
else :
    print(Erreur)