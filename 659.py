def Repeat(x):
    repeated = [] 
    for i in range(len(x)): 
        for j in range(i+1, len(x)): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated
