def odd_Num_Sum(n) : 
    sm = 0
    for i in range(1,n+1) : 
        sm = sm + (2*i-1)*(2*i-1)*(2*i-1)*(2*i-1)*(2*i-1)     
    return sm
