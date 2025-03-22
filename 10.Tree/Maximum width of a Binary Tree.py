from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def widthOfBinaryTree(root: TreeNode) -> int:
    if not root:
        return 0
    
    max_width = 0
    queue = deque([(root, 0)])
    
    while queue:
        level_length = len(queue)
        _, first_pos = queue[0]
        _, last_pos = queue[-1]
        
        max_width = max(max_width, last_pos - first_pos + 1)
        
        for _ in range(level_length):
            node, pos = queue.popleft()
            
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))
    
    return max_width

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    
    print(widthOfBinaryTree(root))
