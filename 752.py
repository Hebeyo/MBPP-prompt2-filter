def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return jacobsthal_num(n-1) + 2*jacobsthal_num(n-2)
