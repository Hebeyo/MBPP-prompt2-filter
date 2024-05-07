def binomial_probability(n, k, p):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    return factorial(n)/(factorial(k)*factorial(n-k)) * p**k * (1-p)**(n-k)
