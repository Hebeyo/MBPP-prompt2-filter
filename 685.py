def sum_Of_Primes(n): 
    primes = [True] * (n + 1)  
    p = 2
    while p * p <= n: 
        if primes[p] == True:  
            i = p * 2
            while i <= n: 
                primes[i] = False
                i += p 
        p += 1    
    sum = 0
    for i in range (2,n + 1): 
        if(primes[i]): 
            sum += i 
    return sum
