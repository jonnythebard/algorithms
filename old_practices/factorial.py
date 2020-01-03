def factorial(n):
    if n == 0:
        return 1
    r = n * factorial(n-1)
    return r
