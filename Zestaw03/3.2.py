# Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort()

# x, y = 1, 2, 3 # Za dużo zmiennych, lub nieprawidlowo podany typ danych
x = y = [1,2,3]

# X = 1, 2, 3 ; X[1] = 4 # Nieprawidlowo podany typ danych
X = [1, 2, 3] ; X[1] = 4

# X = [1, 2, 3] ; X[3] = 4 # Nie ma liczby pod ID 3 (ID zaczyna sie od 0)
X = [1,2,3] ; X.append(4)

# X = "abc" ; X.append("d") # list.append nie dziala dla type'a str
X = "abc"; X = list(X) ; X.append("d") ; X = str(X)

# L = list(map(pow, range(8))) # Nie do konca rozumiem co Pan chce zrobic, ale..
# pow() potrzebuje 2 zmiennych. Dzialanie: pow(a,b) = a**b