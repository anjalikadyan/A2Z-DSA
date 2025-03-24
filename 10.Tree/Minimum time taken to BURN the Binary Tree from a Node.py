from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while i < len(values):
        node = queue.popleft()
        
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def build_parent_map(root, parent_map):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            parent_map[node.left] = node
            queue.append(node.left)
        if node.right:
            parent_map[node.right] = node
            queue.append(node.right)

def find_target(root, target):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == target:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None

def min_time_to_burn(root, target):
    if not root:
        return 0
    
    parent_map = {}
    build_parent_map(root, parent_map)
    target_node = find_target(root, target)
    if not target_node:
        return -1  
    
    visited = set()
    queue = deque([(target_node, 0)])
    visited.add(target_node)
    max_time = 0
    
    while queue:
        node, time = queue.popleft()
        max_time = max(max_time, time)
        
        for neighbor in (node.left, node.right, parent_map.get(node)):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, time + 1))
    
    return max_time

values = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5
root = build_tree(values)
print(min_time_to_burn(root, target))
