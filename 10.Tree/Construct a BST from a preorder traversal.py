from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None
    
    def construct_bst(bound: int) -> Optional[TreeNode]:
        nonlocal index
        if index == len(preorder) or preorder[index] > bound:
            return None
        
        root = TreeNode(preorder[index])
        index += 1
        root.left = construct_bst(root.val)
        root.right = construct_bst(bound)
        return root
    
    index = 0
    return construct_bst(float('inf'))

def print_inorder(root: Optional[TreeNode]):
    if root:
        print_inorder(root.left)
        print(root.val, end=' ')
        print_inorder(root.right)

preorder = [8, 5, 1, 7, 10, 12]
root = bstFromPreorder(preorder)
print_inorder(root)  
