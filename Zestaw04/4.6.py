# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
# która może zawierać zagnieżdżone podsekwencje. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, 
# czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).


def sum_seq(L):
    for i in L:
        if isinstance(i, (list, tuple)):
            L[L.index(i)] = sum(i)
    return L


def main():
    L = [1,2,3,[1,3,7,7],5,7,(2,5,3),6,7]
    answer = sum(sum_seq(L))
    print(answer)

if __name__ == "__main__":
    main()