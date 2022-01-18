from random import randint, gauss, shuffle
from math import ceil, floor
from numpy import concatenate

# różne liczby int od 0 do N-1 w kolejności losowej
def rand_array_nsort(n): 
    rand_list = list(range(0,n))
    shuffle(rand_list)
    
    return rand_list



def insertionSort(array):
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
 
        # Move elements of array[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
                array[j + 1] = key

# różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji)
def rand_array_rsort(n):
    array = rand_array_nsort(n)

    # divide whole array into 2 parts(mid_index), then play only with 2 parts;
    # returning in the end sort_first_part + midddle_element + sort_sec_part
    if n % 2 == 1: mid_index = ceil( n / 2)
    else: mid_index = floor(n / 2)

    first_part = [array[j] for j in range(mid_index)]
    second_part = [array[j] for j in range(mid_index + 1, len(array))]

    insertionSort(first_part)
    insertionSort(second_part)
    
    return concatenate((first_part, array[mid_index], second_part), axis=None)

# różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności
def rand_array_rand_sort_reversed(n):
    array = rand_array_nsort(n)
    
    # divide whole array into 2 parts(mid_index), then play only with 2 parts;
    # returning in the end reversed_first_part + midddle_element + reversed_sec_part
    if n % 2 == 1: mid_id = ceil( n / 2)
    else: mid_id = floor(n / 2)

    first_part = [array[j] for j in range(mid_id)]
    second_part = [array[j] for j in range(mid_id + 1, len(array))]

    insertionSort(first_part)
    insertionSort(second_part)
    
    first_part.reverse()
    second_part.reverse()
    
    return concatenate((first_part, array[mid_id], second_part), axis=None)


# N liczb float w kolejności losowej o rozkładzie gaussowskim
def rand_float_gauss(n:int):
    return [gauss(0,1) for j in range(n)]

# N liczb int w kolejności losowej, o wartościach powtarzających się, 
# należących do zbioru k elementowego (k < N, np. k*k = N)
def rand_int_array(n:int):
    array = []
    my_set = rand_array_nsort(randint(1, n - 1))
    
    for j in range(n): 
        array.append(my_set[randint(0,len(my_set) - 1)])

    return array