def average_Even(n):
    sum = 0
    count = 0
    while n >= 2:
        count = count + 1
        sum = sum + n
        n = n - 2
    return sum // count
