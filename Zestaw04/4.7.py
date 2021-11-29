# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. 
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, 
# wykonać przez isinstance(item, (list, tuple)).

def flatten(sequence):          #metoda rekurencyjna
    result = []
    if isinstance(sequence, (list,tuple)) == True:
        for item in sequence:
            if isinstance(item, (list, tuple)) == True:
                for obj in flatten(item):
                    result.append(obj)
            else:
                result.append(item)

    else:
        result.append(sequence)
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))