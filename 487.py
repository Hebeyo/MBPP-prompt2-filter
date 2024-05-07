def sort_tuple(tup): 
    for i in range(0, len(tup)): 
        for j in range(i+1, len(tup)): 
            if (tup[i][-1] > tup[j][-1]): 
                temp = tup[i] 
                tup[i]= tup[j] 
                tup[j]= temp 
    return tup
