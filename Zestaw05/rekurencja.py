from math import prod

def fibonacci(n):
    a = 0
    b = 1

    accum = 1
    while accum < n:
        b += a
        a = b-a
        accum += 1

    return b

def silnia(n):
    odp = prod([i for i in range(n+1) if i != 0])
    return odp