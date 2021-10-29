import math
import unittest

class Point:
	"""Klasa reprezentujaca punkty na plaszczyznie."""
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return "("+repr(self.x)+", "+repr(self.y)+")"

	def __repr__(self):
		return self.__class__.__name__ + "("+repr(self.x)+", "+repr(self.y)+")"

	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

	def __ne__(self, other):
		if self.x != other.x or self.y != other.y:
			return True
		else:
			return False

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return self.x * other.x + self.y * other.y

	def cross(self, other):
		return self.x * other.y - self.y * other.x

	def length(self):
		return math.sqrt(self.x ** 2.0 + self.y ** 2.0)

p1 = Point(2,3)
p2 = Point(3,4)
 
 
class TestPoint(unittest.TestCase):
	def test__str__(self):
		self.assertEqual(p1.__str__(),"(2, 3)")
	def test__repr__(self):
		self.assertEqual(p1.__repr__(),"Point(2, 3)")
	def test__eq__(self):
		self.assertFalse(p1.__eq__(p2))
	def test__ne__(self):
		self.assertTrue(p1.__ne__(p2))

	def test__add__(self):
		self.assertEqual(p1.__add__(p2),Point(5,7))
	def test__sub__(self):
		self.assertEqual(p1.__sub__(p2),Point(-1,-1))
	def test__mul__(self):
		self.assertEqual(p1.__mul__(p2),18)
	def testcross(self):
		self.assertEqual(p1.cross(p2),-1)
	def testlength(self):
		self.assertEqual(p1.length(),math.sqrt(13))

if __name__ == '__main__':
	unittest.main()     