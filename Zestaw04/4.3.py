# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
def factorial(n):
	wynik  = 1
	for i in range(1 , n+1): 
		wynik = wynik * i
	return wynik

print(factorial(int(input("Podaj liczbe: "))))