# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. 
# Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

a = "Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line"
a = a.split()

first = ""
last = ""

for i in a:
    i = list(i)
    first += i[0]
    last += i[-1]

print("First: ", first, "\nLast: ", last)