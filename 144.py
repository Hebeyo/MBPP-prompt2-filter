def sum_Pairs(arr,n):
    sum = 0
    for i in range(n):
        sum += i*arr[i] - (n-1-i) * arr[i]
    return sum
