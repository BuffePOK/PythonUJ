# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. 
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- 
# i dwucyfrowe będą miały blok dopełniony zerami, 
# np. 007, 024. Wskazówka: str.zfill().

L = [1,2,34,345,12,98,644,34,744,456,2,444,77,234,7,77,0,00,000,10,100]

for l in L:
    id = L.index(l)
    l = str(l)
    l = str.zfill(l,3)
    L[id] = l

print(L)