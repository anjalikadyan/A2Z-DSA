from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not postorder:
        return None
    
    root_val = postorder.pop()  
    root = TreeNode(root_val)
    
    inorder_index = inorder.index(root_val)  
    root.right = buildTree(inorder[inorder_index + 1 :], postorder)
    root.left = buildTree(inorder[:inorder_index], postorder)
    
    return root

def print_preorder(root: Optional[TreeNode]):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result

def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)

def findMin(root: Optional[TreeNode]) -> Optional[int]:
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = buildTree(inorder, postorder)
print("Preorder Traversal:")
print_preorder(root)
print("\nInorder Traversal:")
print(inorderTraversal(root))

search_val = 15
found_subtree = searchBST(root, search_val)
print("\nSubtree rooted at searched value:")
print_preorder(found_subtree)

min_value = findMin(root)
print("\nMinimum value in BST:", min_value)
