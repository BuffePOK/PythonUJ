# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L. 
L = [-50,0,1,2,3,4,7,6,5,10,123,11,12,13,8,9]
L.sort()
ans = []

L.append("NULL")

for l in L:
    if l == "NULL":
        break

    id = L.index(l)

    if L[id]+1 == L[id+1] and L[id]-1 == L[id-1]:
        ans.append(L[id-1])
        ans.append(L[id])
        ans.append(L[id+1])
        ans = list(set(ans))

print(ans)