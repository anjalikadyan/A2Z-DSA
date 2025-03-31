import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtree(root):
    def helper(node):
        if not node:
            return (True, 0, float('inf'), float('-inf')) 
        leftIsBST, leftSize, leftMin, leftMax = helper(node.left)
        rightIsBST, rightSize, rightMin, rightMax = helper(node.right)
        
        if leftIsBST and rightIsBST and leftMax < node.val < rightMin:
            size = leftSize + rightSize + 1
            return (True, size, min(leftMin, node.val), max(rightMax, node.val))
        
        return (False, max(leftSize, rightSize), 0, 0)
    
    return helper(root)[1]

def build_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    return root

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)  
    root = build_tree()
    print("Size of the largest BST subtree:", largestBSTSubtree(root))
