# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

L = 784561302507845612121354560214500064113201030015310321036036103651302135032103540321032103210321036513215610231023103210310321023103210
L = list(str(L))
accum = 0
for i in L:
    if i == "0":
        accum += 1

print(accum)