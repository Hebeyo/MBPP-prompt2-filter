def length_Of_Last_Word(a): 
    l = 0
    x = a.split() 
    if len(x) == 0:
        return 0
    return len(x[-1])
