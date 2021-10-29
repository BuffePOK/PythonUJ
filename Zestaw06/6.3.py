# W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. 
# Prostokąt jest określony przez podanie dwóch wierzchołków, lewego dolnego i prawego górnego.
#  Napisać kod testujący moduł rectangles.

from point import Point
import unittest

class Rectangle:
	"""Klasa reprezentujaca prostokat na plaszczyznie."""

	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)
	def __str__(self):
		return "[("+repr(self.pt1.x)+", "+repr(self.pt1.y) +", " + repr(self.pt2.x)+", "+repr(self.pt2.y)+ ')]'
	def __repr__(self):
		return "Rectangle("+repr(self.pt1.x)+", "+repr(self.pt1.y) +", " + repr(self.pt2.x)+", "+repr(self.pt2.y)+ ')'

	def __eq__(self, other):
		if self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y :
			return True
		else:
			return False
	def __ne__(self, other): 
		if self.pt1.x != other.pt1.x or self.pt1.y != other.pt1.y or self.pt2.x != other.pt2.x or self.pt2.y != other.pt2.y :
			return True
		else:
			return False

	def center(self):
		return Point((self.pt1.x +self.pt2.x)/2 , (self.pt1.y + self.pt2.y)/2)
	def area(self):
		return (abs(self.pt1.x-self.pt2.x) * abs(self.pt1.y-self.pt2.y))
	def move(self, x, y):
		return(Rectangle(self.pt1.x+x , self.pt1.y+y , self.pt2.x+x , self.pt2.y+y))
        

r1 = Rectangle(0,0,2,2)
r2 = Rectangle(2,0,4,2)

print(r1.__repr__())
print(r1.__str__())



class TestRectangle(unittest.TestCase):
	def test__str__(self):
		self.assertEqual(r1.__str__(), "[(0, 0, 2, 2)]")
	def test__repr__(self):
		self.assertEqual(r1.__repr__(),"Rectangle(0, 0, 2, 2)")
	def test__eq__(self):
		self.assertTrue(r1 == Rectangle(0,0,2,2))
		self.assertFalse(r2 == Rectangle(0,0,2,2))
	def test__ne__(self):
		self.assertFalse(r1 != Rectangle(0,0,2,2))
		self.assertTrue(r1 != r2)
	def testcenter(self):
		self.assertEqual(r1.center(),Point(1,1))
	def testarea(self):
		self.assertEqual(r1.area(),4)
	def testmove(self):
		self.assertEqual(r1.move(1,1),Rectangle(1,1,3,3))

if __name__ == '__main__':
	unittest.main() 