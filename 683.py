def sum_Square(n) : 
    for i in range(1, int(n ** 0.5) + 1) : 
        for j in range(1, int(n ** 0.5) + 1) : 
            if (i * i + j * j == n) : 
                return True
    return False
