# Format Hours 24 to 12
        
# Time = 3h
# Date = 1 september 2023

import sys
import re


def check_format() :
    
    Check      = re.search(":" ,sys.argv[1])
    Erreur     = 'erreur, please enter yours time like that HH:mm with HH < 25 and mm < 61'
    
    if Check != None :
    
        L0     = False
        L1     = False
        List   = sys.argv[1].split(":")

        if len(sys.argv) == 2 :
            L0 = List[0].isdigit()
            L1 = List[1].isdigit()
            
        if L0 == True and L1 == True and int(List[0]) < 25 and int(List[1]) < 61 and len(List[0]) == 2 and len(List[1]) == 2:
            return True
        else :
            print(Erreur)
    else :
        print(Erreur)
    return False

        
if len(sys.argv) == 2 and check_format() == True :
    
    List    = sys.argv[1].split(":")
    Mod     = [0,List[1],0]
    Out     = ''

    if int(List[0]) >= 12 :
        Mod[0] = int(List[0]) - 12
        Mod[2] = 'PM'
    else :
        Mod[0] = List[0]
        Mod[2] = 'AM'
        
    if int(List[0]) == 0 or int(List[0]) == 12 :
        Mod[0] = 12
    else :
        Mod[0] = List[0]
        
    print(Mod[0], end=':') 
    print(Mod[1], end='')
    print(Mod[2])
