from random import randint

class RandomQueue:

    def __init__(self, size): 
        self.elem = []
        self.numOfElem = 0
        self.size = size
        self.tail = -1

    def isEmpty(self):
        return self.numOfElem == 0

    def is_full(self): 
        return self.numOfElem == self.size

    def clear(self): # czyszczenie listy
        self.elem = []
        
    def insert(self, item): 
        if item != None and self.size > self.numOfElem:
            self.elem.append(item)
            self.numOfElem += 1
            self.tail += 1

    def remove(self): # zwraca losowy element        
        index = randint(0, self.numOfElem)
        
        tmp = self.elem[index]
        tmp2 = self.elem[self.tail]

        self.elem[self.tail] = tmp

        self.elem[index] = tmp2

        out = self.elem.pop(self.tail)
        self.tail -= 1
        self.numOfElem -= 1

        return out

    def str(self):
        o = ''
        for i in self.elem: o += str(i);o += ', '
        
        return o[:-2]

if __name__ == '__main__':
    rand_queue = RandomQueue(5)

    print(rand_queue.isEmpty())

    rand_queue.insert(12)
    print(rand_queue.isEmpty())
    rand_queue.insert(11)
    rand_queue.insert(10)
    rand_queue.insert(9)
    
    print(rand_queue.str())

    rand_queue.insert(8)

    print(rand_queue.str())
    print(rand_queue.is_full())

    rand_queue.remove()
    print(rand_queue.str())

    rand_queue.remove()
    print(rand_queue.str())