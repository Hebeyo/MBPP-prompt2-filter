def floor_Min(A,B,N):
    x = N
    if B > N:
        x = B - 1
    return (A*x) // B
