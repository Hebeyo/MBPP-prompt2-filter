def count_Primes_nums(n):
    count = 0
    for num in range(2, n):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1
    return count
