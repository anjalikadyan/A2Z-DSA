from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildGraph(node, parent, graph):
    if not node:
        return
    if parent:
        graph[node.val].append(parent.val)
        graph[parent.val].append(node.val)
    buildGraph(node.left, node, graph)
    buildGraph(node.right, node, graph)

def distanceK(root: TreeNode, target: TreeNode, k: int):
    graph = defaultdict(list)
    buildGraph(root, None, graph)
    
    queue = deque([(target.val, 0)])
    visited = set()
    visited.add(target.val)
    result = []
    
    while queue:
        node, dist = queue.popleft()
        if dist == k:
            result.append(node)
        if dist > k:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    
    return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    target = root.left
    k = 2
    print(distanceK(root, target, k))
