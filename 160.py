def solution(a, b, n):
    for i in range(n//a + 1):
        if (n - i * a) % b == 0:
            return ('x = ', i, ', y = ', (n - i * a) // b)
    return 'No solution'
