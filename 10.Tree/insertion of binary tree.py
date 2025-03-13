class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = Node(data)
                break
            else:
                queue.append(temp.left)
            
            if not temp.right:
                temp.right = Node(data)
                break
            else:
                queue.append(temp.right)
    
    def display(self):
        if not self.root:
            return "Tree is empty"
        
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.data, end=' ')
            
            if temp.left:
                queue.append(temp.left)
            
            if temp.right:
                queue.append(temp.right)
        print()
n = int(input("Enter the number of nodes: "))
root_data = int(input("Enter the root node: "))
ob = BinaryTree(root_data)

for _ in range(n - 1):
    a = int(input("Enter the node: "))
    ob.insert(a)

print("Tree (Level-order):")
ob.display()
