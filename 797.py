def sum_in_Range(l,r):
    sum1 = 0
    for i in range(l,r+1):
        if i%2 != 0:
            sum1 += i
    return sum1
