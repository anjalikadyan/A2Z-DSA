class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSumProperty(root: TreeNode) -> int:
    if not root:
        return 1
    
    if not root.left and not root.right:
        return 1
    
    left_val = root.left.val if root.left else 0
    right_val = root.right.val if root.right else 0
    
    if root.val != left_val + right_val:
        return 0
    
    return isSumProperty(root.left) and isSumProperty(root.right)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    
    print(isSumProperty(root))
