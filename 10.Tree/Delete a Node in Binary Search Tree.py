class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None
    
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    
    return root

def minValueNode(node):
    current = node
    while current and current.left:
        current = current.left
    return current

def insertNode(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insertNode(root.left, key)
    else:
        root.right = insertNode(root.right, key)
    
    return root

def inorderTraversal(root: TreeNode):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)

root = None
values = [50, 30, 70, 20, 40, 60, 80]
for val in values:
    root = insertNode(root, val)

print("Inorder before deletion:")
inorderTraversal(root)
print()

key_to_delete = 50
root = deleteNode(root, key_to_delete)

print("Inorder after deletion:")
inorderTraversal(root)
print()
