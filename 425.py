def count_element_in_list(list1, x): 
    ctr = 0
    for i in list1: 
        if x in i: 
            ctr+= 1          
    return ctr
