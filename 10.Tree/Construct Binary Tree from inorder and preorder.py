from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    root_index = inorder.index(root_val)
    
    root.left = buildTree(preorder[1:root_index+1], inorder[:root_index])
    root.right = buildTree(preorder[root_index+1:], inorder[root_index+1:])
    
    return root

def printTree(root: Optional[TreeNode]):
    if not root:
        return
    print(root.val, end=' ')
    printTree(root.left)
    printTree(root.right)

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
tree = buildTree(preorder, inorder)
printTree(tree)
