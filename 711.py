def product_Equal(n): 
    n = str(n)
    odd = 1
    even = 1
    for i in range(0, len(n)):
        if i % 2 == 0:
            odd *= int(n[i])
        else:
            even *= int(n[i])
    if odd == even:
        return True
    return False
