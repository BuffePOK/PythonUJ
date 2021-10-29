# Napisać funkcję odwracanie(L, left, right) 
# odwracającą kolejność elementów na liście od numeru left do right włącznie. 
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

from random import randint

def odwracanie(L, left, right):
    
    L[left:right] = L[left:right][::-1]

    return L


def main():
    n = int(input("Podaj ilosc liczb w liscie: "))
    lista = [randint(1, 100) for i in range(n)]

    first_ID = int(input("Podaj ID left: "))
    second_ID = int(input("Podaj ID right: ")) + 1

    print("Zgenerowana lista: ", lista)

    iter = odwracanie(lista, first_ID, second_ID)

    print(iter)

if __name__ == "__main__":
    main()