class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

# Wersja rekurencyjna

def count_leafs(top):
    result = 0
    if top.left != None:
        result += count_leafs(top.left)
    if top.right != None:
        result += count_leafs(top.right)
    if top.left == None and top.right == None:
        return 1
    return result

def count_total(top):
    if top.left == None and top.right == None:
        return 1
    result = 1
    if top.left != None:
        result += count_total(top.left)
    if top.right != None:
        result += count_total(top.right)
    return result

# Ręczne budowanie drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(count_leafs(root))
print(count_total(root))