# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
from math import prod
def silnia(n):
    odp = prod([i for i in range(n+1) if i != 0])
    return odp

def main():
    answer = int(input("Napisz liczbe: "))
    answer = silnia(answer)
    print(answer)

if __name__ == "__main__":
    main()