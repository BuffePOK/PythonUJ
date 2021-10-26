# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim 
# (z literami I, V, X, L, C, D, M) na liczby arabskie 
# (podać kilka sposobów tworzenia takiego słownika). 
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

R = {
     'I': 1, 
     'V': 5, 
     'X': 10, 
     'L': 50, 
     'C': 100, 
     'D': 500, 
     'M': 1000}

s = input()
prev = s[-1]
res = R[prev]

for cur in s[-2::-1]:
    if R[cur] >= R[prev]:
        res += R[cur]
    else:
        res -= R[cur]
    prev = cur

print(res)