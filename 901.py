def smallest_multiple(n):
    if n==1:
        return 1
    i = n
    while True:
        for a in range(1, n+1):
            if i % a != 0:
                i += n
                break
            if a == n:
                return i
