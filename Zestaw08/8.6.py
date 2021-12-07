#przy obliczaniu funkcji z duzymi parametrami metoda rekurencyjna jest bardzo niewydajna.


def p_rekurencja(i,j):
    if i < 0 or j < 0:
        raise ValueError("Incorrect data")
    if j == 0:
        return 0.0
    elif i == 0:
        return 1.0
    elif i == 0 and j == 0:
        return 0.5
    else:
        return 0.5 * (p_rekurencja(i, j-1) + p_rekurencja(i-1, j))


def p_dynamicznie(i, j):
    if i < 0 or j < 0:
        raise ValueError("Incorrect data")

    values = {}
    for x in range(0, i+1):
        for y in range(0, j+1):
            if x == 0 and y == 0:
                values[(x, y)] = 0.5
            if x == 0:
                values[(x, y)] = 1.0
            elif y == 0:
                values[(x, y)] = 0.0
            else:
                values[(x, y)] = 0.5 * (values[(x, y-1)] + values[(x-1, y)])

    return values[(i, j)]


print(p_dynamicznie(8, 4))
print(p_rekurencja(8, 4))
