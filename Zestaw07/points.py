import unittest
import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):    # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
        return self.x*other.x + self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_print(self):
        self.assertEqual(Point(4, 2).__str__(), "(4, 2)")
        self.assertEqual(Point(2, 6).__str__(), "(2, 6)")
        self.assertEqual(Point(1, 2).__repr__(), "Point(1, 2)")
        self.assertEqual(Point(6, 4).__repr__(), "Point(6, 4)")

    def test_cmp(self):
        self.assertTrue(Point(5,1) == Point(5, 1))
        self.assertTrue(Point(3,6) == Point(3, 6))
        self.assertTrue(Point(1,6) != Point(3, 6))
        self.assertTrue(Point(1,6) != Point(8, 6))

    def test_add(self):
        self.assertEqual(Point(4, 1) + Point(3, 5), Point(7, 6))
        self.assertEqual(Point(3, 7) + Point(7, 5), Point(10, 12))

    def test_sub(self):
        self.assertEqual(Point(6, 1) - Point(3, 0), Point(3, 1))
        self.assertEqual(Point(3, 5) - Point(5, 8), Point(-2, -3))

    def test_mul(self):
        self.assertEqual(Point(4, 5) * Point(3, 4), 32)
        self.assertEqual(Point(2, 1) * Point(3, 2), 8)

    def test_cross(self):
        self.assertEqual(Point(5, 1).cross(Point(-2, 4)), 22)
        self.assertEqual(Point(2, 1).cross(Point(-2, 4)), 10)
        self.assertEqual(Point(6, 8).cross(Point(6, 8)), 0)

    def test_len(self):
        self.assertEqual(Point(4, 3).length(), 5)
        self.assertEqual(Point(-2, -3).length(), math.sqrt(13))

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()