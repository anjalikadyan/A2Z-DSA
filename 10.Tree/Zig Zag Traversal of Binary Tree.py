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

    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]
        left_to_right = True
        
        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            if not left_to_right:
                level.reverse()
            result.append(level)
            queue = next_queue
            left_to_right = not left_to_right
        
        return result


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
solution = Solution()
print(solution.isBalanced(root1))  
print(solution.diameterOfBinaryTree(root1))  
print(solution.isSameTree(root1, root2))  
print(solution.zigzagLevelOrder(root1)) 
