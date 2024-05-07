def set_Right_most_Unset_Bit(n): 
    if (n == 0): 
        return 1
    if ((n & (n + 1)) == 0):     
        return n 
    pos = 1
    while((n & (1 << pos))): 
        pos += 1
    return (n | (1 << pos))
