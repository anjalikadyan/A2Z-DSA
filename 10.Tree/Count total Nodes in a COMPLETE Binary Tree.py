class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree_height(root):
    height = 0
    while root:
        height += 1
        root = root.left
    return height

def count_nodes(root):
    if not root:
        return 0
    
    left_height = get_tree_height(root.left)
    right_height = get_tree_height(root.right)
    
    if left_height == right_height:
        return (1 << left_height) + count_nodes(root.right)
    else:
        return (1 << right_height) + count_nodes(root.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(count_nodes(root))  
