class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  
            return max(left_height, right_height) + 1
        
        return height(root) != -1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
solution = Solution()
print(solution.isBalanced(root)) 
