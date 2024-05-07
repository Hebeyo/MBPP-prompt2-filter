def divisible_by_digits(startnum, endnum):
    res = []
    for n in range(startnum, endnum+1):
        if all([int(x) != 0 and n%int(x) == 0 for x in str(n)]):
            res.append(n)
    return res
