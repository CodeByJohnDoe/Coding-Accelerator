# 2 twins sequence
        
# Time = 1h30
# Date = 26 september 2023

def sequence():    

    list_number_i = []
    list_number_j = []
    
    START_SEQUENCE = 0
    END_SEQUENCE = 99
    
    for i1 in range (10) :
        for i2 in range (10) :
            
            for j1 in range (10) :
                for j2 in range(10) :
                    
                    sum_i = i1*10 + i2
                    sum_j = j1*10 + j2
                    
                    if sum_i < sum_j :
    
                        list_number_i.append(f"{i1}{i2}")
                        list_number_j.append(f"{j1}{j2}")
                    
    result = ', '.join(f"{i} {j}" for i, j in zip(list_number_i, list_number_j))
    
    print(result)

sequence()