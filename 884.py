def all_Bits_Set_In_The_Given_Range(n,l,r):
    for i in range(l,r+1):
        if n & (1 << (i-1)) == 0:
            return False
    return True
