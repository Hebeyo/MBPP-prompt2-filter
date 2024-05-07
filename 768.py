def check_Odd_Parity(x): 
    parity = 0
    while (x != 0): 
        parity += 1
        x = x & (x - 1) 
    if (parity % 2 == 1): 
        return True
    else: 
        return False
