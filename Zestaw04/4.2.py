# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, 
# które zwracają pełny string przez return. 
# Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n):
    if n < 0:
        print("Impossible")
        
    part = "|...."
    answer = ""
    accum = 0

    while accum < n:
        answer += part
        accum += 1
    answer += "|\n"
    accum = 0

    while accum < n:
        if accum >= 0 and accum < 10:
            answer += str(accum) + "    "
        elif accum >= 10:
            answer += str(accum) + "   "
        accum += 1
    answer += str(accum)

    return answer

def make_grid(rows, cols):
    


    line1 = "+---"
    line2 = "|   "
    accum_vertical = 0

    answer = ""

    accum_horizontal = 0
    while accum_horizontal < cols:
            answer += line1
            accum_horizontal += 1
    answer += "+\n"
    accum_horizontal = 0

    while accum_vertical < rows:
        while accum_horizontal < cols:
            answer += line2
            accum_horizontal += 1
        answer += "|\n"

        accum_horizontal = 0
        while accum_horizontal < cols:
            answer += line1
            accum_horizontal += 1
        answer += "+\n"

        accum_horizontal = 0
        accum_vertical += 1

    return answer
    
def main():
    n = int(input("Wpisz liczbę: "))
    ans = make_ruler(n)
    print(ans)

    rows, cols = input("Podaj macierz(AxB): ").split("x")
    rows, cols = int(rows), int(cols)
    ans = make_grid(rows, cols)
    print(ans)

if __name__ == "__main__":
    main()