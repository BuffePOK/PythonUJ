# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
# która może zawierać zagnieżdżone podsekwencje. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, 
# czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).


def sum_seq(sequence):
	if isinstance(sequence , (list, tuple)):
		return  sum(map(sum_seq , sequence))
	return sequence

L=(1,2,3,[5,5])
print(L)
print(sum_seq(L))