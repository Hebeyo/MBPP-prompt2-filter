def differ_At_One_Bit_Pos(a,b):
    count = 0
    while a or b:
        if a & 1 != b & 1:
            count += 1
        a >>= 1
        b >>= 1
    return count == 1
