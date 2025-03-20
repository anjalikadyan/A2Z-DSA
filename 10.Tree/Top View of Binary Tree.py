from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def top_view(root):
    if not root:
        return []
    
    queue = deque([(root, 0)])  
    hd_node_map = {}
    
    while queue:
        node, hd = queue.popleft()
        
        if hd not in hd_node_map:
            hd_node_map[hd] = node.val
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    return [hd_node_map[hd] for hd in sorted(hd_node_map.keys())]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

print(top_view(root))
