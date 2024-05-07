def get_pell(n): 
    pell = [0] * (n + 1)
    pell[0] = 0
    pell[1] = 1
    for i in range(2, n + 1):
        pell[i] = 2 * pell[i - 1] + pell[i - 2]
    return pell[n]
