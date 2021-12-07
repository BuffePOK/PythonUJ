class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self): # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

# nowe metody

    def search(self, data):     # Zwraca łącze do węzła o podanym kluczu lub None.
        if self.length != 0:
            if self.head.data == data:
                return self.head
            node = self.head
            while node.next != None:
                if node.next.data == data:
                    break
                node = node.next
            return node.next
        return None



    def find_min(self):     # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.length != 0:
            node = self.head
            minLink = node
            while node.next != None:
                if node.next.data < minLink.data:
                    minLink = node.next
                node = node.next
            return minLink
        return None



    def find_max(self):     # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.length != 0:
            node = self.head
            maxLink = node
            while node.next != None:
                if node.next.data > maxLink.data:
                    maxLink = node.next
                node = node.next
            return maxLink
        return None



    def reverse(self):       # Odwracanie kolejności węzłów na liście.
        if self.length == 0:
            return self
        reversed = SingleList()
        while self.head != None:
            reversed.insert_head(self.remove_head())
        while reversed.head != None:
            self.insert_tail(reversed.remove_head())




alist = SingleList()
alist.insert_head(Node(11))
alist.insert_head(Node(110))
alist.insert_head(Node(1))
alist.insert_head(Node(-1))
alist.insert_head(Node(100))
alist.insert_tail(Node(33))
print ( "length {}".format(alist.length) )
print ( "length {}".format(alist.count()) )
print("łącze do 22: {}".format(alist.search(22)))
print("minLink: {}".format(alist.find_min()))
print("maxLink: {}".format(alist.find_max()))
# 100 -1 1 11- 11 33
alist.reverse()
while not alist.is_empty():
    print ( "remove head {}".format(alist.remove_head()) )