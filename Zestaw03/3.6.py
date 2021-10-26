# Napisać program rysujący prostokąt zbudowany z małych kratek. 
# Należy zbudować pełny string, a potem go wypisać. 

vertical, horizontal = input("Podaj macierz(AxB): ").split("x")
vertical, horizontal = int(vertical), int(horizontal)


line1 = "+---"
line2 = "|   "
accum_vertical = 0

answer = ""

accum_horizontal = 0
while accum_horizontal < horizontal:
        answer += line1
        accum_horizontal += 1
answer += "+\n"
accum_horizontal = 0

while accum_vertical < vertical:
    while accum_horizontal < horizontal:
        answer += line2
        accum_horizontal += 1
    answer += "|\n"

    accum_horizontal = 0
    while accum_horizontal < horizontal:
        answer += line1
        accum_horizontal += 1
    answer += "+\n"

    accum_horizontal = 0
    accum_vertical += 1


print(answer)
