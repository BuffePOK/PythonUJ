from math import gcd
import unittest


def add_frac(frac1, frac2):       # frac1 + frac2
	
	nww = frac1[1] * frac2[1] / gcd(frac1[1]  , frac2[1])
	mianownik = nww
	licznik = frac1[0] * nww / frac1[1] + frac2[0] * nww / frac2[1]
	
	return [licznik,mianownik]


def sub_frac(frac1, frac2):        # frac1 - frac2

	nww = frac1[1] * frac2[1] / gcd(frac1[1]  , frac2[1])
	mianownik = nww
	licznik = frac1[0] * nww / frac1[1] - frac2[0] * nww / frac2[1]
	
	return [licznik,mianownik]


def mul_frac(frac1, frac2):        # frac1 * frac2
	
	licznik = frac1[0] * frac2[0]
	mianownik = frac1[1] * frac2[1]

	return [licznik,mianownik]


def div_frac(frac1, frac2):        # frac1 / frac2
	
	licznik = frac1[0] * frac2[1]
	mianownik = frac1[1] * frac2[0]

	return [licznik,mianownik]


def is_positive(frac):            # bool, czy dodatni
	
	if (frac[0] >= 0) ^ (frac[1] >= 0):
		return False
	elif (frac[0] <= 0) ^ (frac[1] <= 0):
		return False
	else :
		return True


def is_zero(frac):                # bool, typu [0, x]

	if frac[0] == 0 :
		return True
	else :
		return False


def cmp_frac(frac1, frac2):         # -1 | 0 | +1

	if frac1[0]/frac1[1] < frac2[0]/frac2[1] : 
		return -1
	elif(frac1[0]==frac2[0]): 
		return 0
	elif frac1[0]/frac1[1] > frac2[0]/frac2[1] : 
		return 1


def frac2float(frac):              # konwersja do float
	return frac[0]/frac[1]

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznacznosc)
f5 = [0, 2]                   # zero (niejednoznacznosc)

print ("Start")



class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self): self.assertEqual(mul_frac([1, 2], [1, 2]), [1, 4])

    def test_div_frac(self): self.assertEqual(div_frac([1, 2], [1, 2]), [2, 2])

    def test_is_positive(self): self.assertTrue(is_positive([1,2]))

    def test_is_zero(self): self.assertTrue(is_zero([0,1]))

    def test_cmp_frac(self): self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)

    def test_frac2float(self): self.assertEqual(frac2float([1, 2]), 1/2)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy