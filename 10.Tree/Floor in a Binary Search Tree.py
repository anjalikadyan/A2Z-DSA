class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def findFloor(root, key):
    floor = -1
    while root:
        if root.data == key:
            return root.data
        elif root.data > key:
            root = root.left
        else:
            floor = root.data
            root = root.right
    return floor



root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

key = 13
print("Floor of", key, "is:", findFloor(root, key))
