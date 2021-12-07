from math import sqrt
from random import uniform


def calc_pi(n=100):
    if n==0:
        raise ValueError("Argument error")
    pointsInCircle = 0.0

    for i in range(0,n):
        x = uniform(0,1)
        y = uniform(0,1)

        odl = sqrt(x ** 2 + y ** 2)
        if odl <= 1:
            pointsInCircle += 1

    return (4*pointsInCircle)/n


print(calc_pi())
print(calc_pi(1000))
print(calc_pi(50000))
print(calc_pi(1500000))
print(calc_pi(900000000))