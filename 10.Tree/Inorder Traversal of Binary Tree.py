from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createTree(self, root, l):
        if not l:
            return None
        
        root = TreeNode(l[0])
        queue = deque([root])
        i = 1
        
        while i < len(l):
            current = queue.popleft()
            
            if i < len(l) and l[i] is not None:
                current.left = TreeNode(l[i])
                queue.append(current.left)
            i += 1
            
            if i < len(l) and l[i] is not None:
                current.right = TreeNode(l[i])
                queue.append(current.right)
            i += 1
        
        return root

def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

nodes = [1, 2, 3, 4, 5, 6, 7]  
solution = Solution()
root = solution.createTree(None, nodes)
print("Inorder Traversal:", inorderTraversal(root))
