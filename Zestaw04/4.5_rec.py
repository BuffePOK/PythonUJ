#Napisać funkcję odwracanie(L, left, right) 
# odwracającą kolejność elementów na liście od numeru left do right włącznie. 
# Lista jest modyfikowana w miejscu (in place). 
# Rozważyć wersję iteracyjną i rekurencyjną.

def reverseList(L, left, right):
    
    if left < 0 or left > len(L) - 2 or right < 1 or right > len(L) - 1 or left >= right: 
        return

    L[left], L[right] = L[right], L[left]
    
    reverseList(L, left + 1, right - 1)


def main():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reverseList(L, 0, 9)
    print(L)

if __name__ == '__main__':
    main()