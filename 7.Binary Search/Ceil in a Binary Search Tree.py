class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to insert a node in BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def findCeil(root, key):
    ceil = -1
    while root:
        if root.key == key:
            return root.key
        elif root.key < key:
            root = root.right
        else:
            ceil = root.key
            root = root.left
    return ceil

if __name__ == "__main__":
    root = None
    keys = [8, 4, 12, 2, 6, 10, 14]
    for k in keys:
        root = insert(root, k)

    x = 5
    print("Ceil of", x, "is", findCeil(root, x))  
