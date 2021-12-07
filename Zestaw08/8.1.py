def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if b != 0:
        if a == 0:
            return "Rozwiazanie: (r, {0}), gdzie r nalezy do liczb Rzeczywistych".format(float(-c)/float(b))
        return "Rozwiazanie: (r, {0}r + {1}), gdzie r nalezy do liczb Rzeczywistych".format(float(-a) / float(b), float(-c) / float(b))
    else:
        if a != 0:
            return "Rozwiazanie: ({0}, r), gdzie r nalezy do liczb Rzeczywistych".format(float(-c)/float(a))
        return "blad: {0} != 0".format(c)


print(solve1(40, 4, 5))