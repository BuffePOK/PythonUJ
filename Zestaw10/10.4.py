import unittest

class Queue:
    def __init__(self, size=5):
        #  rozmiar tablicy
        self.n = size + 1
        self.items = self.n * [None]
        # 1 do pobrania 
        self.head = 0
        # 1 wolne
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, elem):
        if not self.is_full():
            self.items[self.tail]= elem
            self.tail = (self.tail + 1) % self.n
        else: return Exception('Queue Overflow!')

    def get(self):
        if not self.is_empty():
            elem = self.items[self.head]
            self.items[self.head] = None # usuwam referencję
            self.head = (self.head + 1) % self.n
            return elem
        else: return Exception('Queue is empty!')

class TestQueue(unittest.TestCase):    
    def test_isEmpty(self):
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        self.assertFalse(q1.is_full())

    def test_isFull(self):
        q2 = Queue(3)
        q2.put(1)
        q2.put(1)
        q2.put(1)

        self.assertTrue(q2.is_full())
        self.assertFalse(q2.is_empty())

    def testPut(self):
        q = Queue(3)
        q.put(5)
        q.put(13)
        self.assertEquals(q.items,[5,13,None,None])

    def testGet(self):
        q = Queue(3)

        q.put(5)
        q.put(13)
        q.get()
        self.assertEquals(q.items,[None,13,None,None])

        q.get()
        self.assertEquals(q.items,[None,None,None,None])

if __name__ == '__main__':
    unittest.main()