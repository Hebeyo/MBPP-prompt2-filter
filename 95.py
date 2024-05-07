def Find_Min_Length(lst):  
    minLength = len(lst[0])
    for i in range(1,len(lst)):
        if len(lst[i]) < minLength:
            minLength = len(lst[i])
    return minLength
