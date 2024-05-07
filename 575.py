def count_no(A,N,L,R): 
    count = 0
    i = L
    while count < N:
        if i % A != 0:
            count += 1
        i += 1
    return i - 1
