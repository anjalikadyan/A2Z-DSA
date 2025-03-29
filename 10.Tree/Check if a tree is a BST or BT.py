class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if not (min_val < root.val < max_val):
        return False
    
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def build_bst_from_list(values):
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    return root

def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None

values = [5, 3, 7, 2, 4, 6, 8]
root = build_bst_from_list(values)
p = TreeNode(2)
q = TreeNode(8)
lca = lowest_common_ancestor(root, p, q)
print(is_valid_bst(root))  
print(inorder_traversal(root))  
print(lca.val if lca else None)  
