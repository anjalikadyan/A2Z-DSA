from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return []
    
    node_queue = deque([(root, 0)])  
    hd_node_map = {}  
    
    while node_queue:
        node, hd = node_queue.popleft()
        hd_node_map[hd] = node.val  
        if node.left:
            node_queue.append((node.left, hd - 1))
        if node.right:
            node_queue.append((node.right, hd + 1))
    
    return [hd_node_map[hd] for hd in sorted(hd_node_map)]

root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(25)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

print(bottom_view(root))  
