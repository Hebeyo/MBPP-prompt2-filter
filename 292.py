def find(n,m):
    q = 0
    while n >= m:
        n -= m
        q += 1
    return q
