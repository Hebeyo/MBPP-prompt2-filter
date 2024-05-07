def jacobsthal_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return jacobsthal_lucas(n - 1) + 2 * jacobsthal_lucas(n - 2)
