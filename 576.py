def is_Sub_Array(A,B,n,m):
    j = 0
    for i in range(n):
        if A[i] == B[j]:
            j += 1
            if j == m:
                return True
        else:
            j = 0
    return False
