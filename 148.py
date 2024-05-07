def sum_digits_twoparts(N) : 
    A = 0
    for i in range(1, N): 
        A = A * 10 + 9
        if A > N: 
            A = A // 10
            break
    B = N - A
    sum1 = 0
    while A: 
        sum1 += A % 10
        A = A // 10
    sum2 = 0
    while B: 
        sum2 += B % 10
        B = B // 10
    return sum1 + sum2
