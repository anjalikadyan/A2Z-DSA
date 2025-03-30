class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    seen = set()
    
    def dfs(node):
        if not node:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)
    
    return dfs(root)

def build_bst_from_list(values):
    if not values:
        return None
    
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root
    
    root = None
    for value in values:
        root = insert_into_bst(root, value)
    return root

values = [5, 3, 6, 2, 4, 7]
k = 9
root = build_bst_from_list(values)
print(findTarget(root, k))  # Output: True
