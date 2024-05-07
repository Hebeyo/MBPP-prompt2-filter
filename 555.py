def difference(n) :  
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1) : 
        sum1 += i * i*i
        sum2 += i
    return sum1 - sum2
