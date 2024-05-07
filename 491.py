def sum_gp(a,n,r):
    total = 0
    for i in range(n):
        total += a
        a *= r
    return total
