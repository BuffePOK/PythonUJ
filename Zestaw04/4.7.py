# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. 
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, 
# wykonać przez isinstance(item, (list, tuple)).

def flatten(seq):
    res = []

    for i in range(len(seq)):
        if isinstance(seq[i], int):
            res.append(seq[i])

        else:
            return flatten(seq[i], res)

    return res            


def main():
    seq = [1, (2, 3), [], [4, (5, 6)], 7]
    seq = flatten(seq)
    print(seq)

if __name__ == '__main__':
    main()