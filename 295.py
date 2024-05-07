def sum_div(number):
    s = 1
    for i in range(2,number):
        if number%i==0:
            s+=i
    return s
