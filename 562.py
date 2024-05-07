def Find_Max_Length(lst):  
    maxLength = 0
    for i in lst:
        if len(i) > maxLength:
            maxLength = len(i)
    return maxLength
