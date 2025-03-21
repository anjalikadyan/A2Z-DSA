class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_symmetric(root):
    if not root:
        return True
    
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
    
    return is_mirror(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric(root)) 
