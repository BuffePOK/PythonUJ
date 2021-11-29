import math

from points import Point
import unittest


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):            # pole powierzchni
        return math.pi * math.pow(self.radius, 2)

    def move(self, x, y):      # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):    # okrąg pokrywający oba
        radius = math.sqrt(math.pow(self.pt.x - other.pt.x, 2) + math.pow(self.pt.y - other.pt.y, 2))
        xCenter = (self.pt.x + other.pt.x) / 2
        yCenter = (self.pt.y + other.pt.y) / 2
        return Circle(xCenter, yCenter, radius)


# Kod testujący moduł.

class TestCircle(unittest.TestCase):
    def setUp(self): pass

    def test_cmp(self):
        self.assertTrue(Circle(1, 1, 5) == Circle(1, 1, 5))
        self.assertFalse(Circle(1, 1, 5) == Circle(1, 2, 5))
        self.assertTrue(Circle(1, 1, 5) != Circle(1, 1, 6))
        self.assertTrue(Circle(1, 6, 5) != Circle(2, 1, 9))
        self.assertFalse(Circle(1, 1, 5) != Circle(1, 1, 5))

    def test_print(self):
        self.assertEqual("Circle(1, 2, 3)", Circle(1, 2, 3).__repr__())
        self.assertEqual("Circle(3, 1, 8)", Circle(3, 1, 8).__repr__())

    def test_area(self):
        self.assertEqual(Circle(1, 1, 5).area(), 25*math.pi)
        self.assertEqual(Circle(1, 1, 2).area(), 4*math.pi)

    def test_move(self):
        self.assertEqual(Circle(1, 2, 3).move(1, 2), Circle(2, 4, 3))
        self.assertEqual(Circle(5, 8, 6).move(3, 5), Circle(8, 13, 6))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 2).cover(Circle(0, 2, 2)), Circle(0, 1, 2))
        self.assertEqual(Circle(0, 0, 2).cover(Circle(2, 2, 2)), Circle(1.0, 1.0, math.sqrt(8)))

    def tearDown(self): pass

if __name__ == '__main__':
	unittest.main() 