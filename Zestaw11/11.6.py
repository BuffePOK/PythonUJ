def partition(array, low, high):
    elem = array[high]
    id = low - 1

    for j in range(low,high):
        if array[j] <= elem:
            id += 1
            array[id], array[j] = array[j], array[id]

    array[id + 1] , array[high] = array[high], array[id + 1]
    return id + 1

def quick_sort(array, low, high):
    stack = [0] * (high - low + 1)
    top = -1

    # dodawanie w stack
    top += 1
    stack[top] = low

    top += 1
    stack[top] = high

    while top >= 0:
        # dostawanie ze stacku
        high1 = stack[top]
        top -= 1

        low1 = stack[top]
        top -= 1

        # pivot element
        pivot = partition(array, low1, high1)

        # jezeli elementy z prawej strony pivot -> dodaj prawa strone w stack
        if pivot + 1 < high1:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = high1
        # jezeli elementy z lewej strony pivot -> dodaj lewa strone w stack
        if pivot - 1 > low1:
            top += 1
            stack[top] = low1
            top += 1
            stack[top] = pivot - 1


array = [19, 13, 5, 2, 1, 7]
quick_sort(array, 0, len(array) - 1)

print ("Sortowany array: " + array.__str__())
