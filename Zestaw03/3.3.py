# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3
L = list(range(31))
print(L)
for i in L:
    if i % 3 != 0:
        print(i)