# Napisać program rysujący "miarkę" o zadanej długości. 
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr 
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
# Należy zbudować pełny string, a potem go wypisać.

# | .
amount = int(input("Wpisz liczbę: "))
if amount < 0:
    print("Impossible")
    
part = "|...."
answer = ""
accum = 0

while accum < amount:
    answer += part
    accum += 1
answer += "|\n"
accum = 0

while accum < amount:
    if accum >= 0 and accum < 10:
        answer += str(accum) + "    "
    elif accum >= 10:
        answer += str(accum) + "   "
    accum += 1
answer += str(accum)

print(answer)