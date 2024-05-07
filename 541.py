def check_abundant(n): 
    sum = 0
    i = 1
    while i <= (n//2): 
        if n%i == 0: 
            sum = sum + i 
        i = i + 1
    return sum > n
