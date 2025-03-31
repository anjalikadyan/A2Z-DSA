class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    first = second = prev = None
    
    def inorder_traverse(node):
        nonlocal first, second, prev
        if not node:
            return
        
        inorder_traverse(node.left)
        
        if prev and node.val < prev.val:
            if not first:
                first = prev
            second = node
        prev = node
        
        inorder_traverse(node.right)
    
    inorder_traverse(root)
    
    if first and second:
        first.val, second.val = second.val, first.val

def inorder_print(root):
    if not root:
        return
    inorder_print(root.left)
    print(root.val, end=' ')
    inorder_print(root.right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2) 
    print("Before recovery:")
    inorder_print(root)
    print()
    
    recoverTree(root)
    
    print("After recovery:")
    inorder_print(root)
    print()
