def is_coprime(x, y):
    for i in range(2, min(x, y)+1):
        if x % i == 0 and y % i == 0:
            return False
    return True
