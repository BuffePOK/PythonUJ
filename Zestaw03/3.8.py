# Dla dwóch sekwencji liczb lub znaków znaleźć: 
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), 
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

from random import randint

# funkca usuwajaca powtarzajace elementy
def KillDuplicateItems(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

L1 = []
L2 = []

# List generator
for i in range(12): L1.append(randint(5,15))
for i in range(12): L2.append(randint(11,21))

# usunac powtarzajace elementy
L1 = KillDuplicateItems(L1)
L2 = KillDuplicateItems(L2)

# 2 listy dla odpowiedziej
La = []
Lb = []

# Dla 1 listy szukamy jednakowe elementy
for obj1 in L1:
    for obj2 in L2:
        if obj1 == obj2:
            La.append(obj1)

# Dla 2 listy jednamy wszystkie elementy
Lb = L1 + L2

# Sprawdzamy, aby nie powtarzaly sie elementy
La = KillDuplicateItems(La)
Lb = KillDuplicateItems(Lb)

print("Punkt A: ", La, "\nPunkt B: ", Lb)