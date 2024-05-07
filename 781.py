def count_Divisors(n) : 
    count = 0
    for i in range(1, n + 1) : 
        if (n % i == 0) : 
            count = count + 1
    if (count % 2 == 0) : 
        return ("Even") 
    else : 
        return ("Odd")
