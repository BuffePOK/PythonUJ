# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    a = 0
    b = 1

    accum = 1
    while accum < n:
        b += a
        a = b-a
        accum += 1

    return b

def main():
    question = int(input("Podaj liczbe dla Fibonacci: "))
    question = fibonacci(question)
    print(question)

if __name__ == "__main__":
    main()