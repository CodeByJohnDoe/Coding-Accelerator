# Size string
        
# Time = 4 h
# Date = 31 aout 2023


import sys

if len(sys.argv) > 1 :
    
    Size    = len(sys.argv)
    Num     = sys.argv[1].isnumeric()
    print(Num)

    if Size == 2 :
        
        if Num == False :
            
            In      = list(sys.argv[1])
            len     = 0
            
            while In != [] :
                del In[0]
                len += 1
            
            print(len)
            
        else :
            print('erreur.3')

    else :
        print('erreur.2')
                            
else :
    print('erreur.1')
    
    