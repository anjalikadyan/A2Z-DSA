def is_safe(node, graph, color, col):
    for neighbor in graph[node]:
        if color[neighbor] == col:
            return False
    return True

def solve(node, graph, m, color):
    if node == len(graph):
        return True

    for col in range(1, m + 1):
        if is_safe(node, graph, color, col):
            color[node] = col
            if solve(node + 1, graph, m, color):
                return True
            color[node] = 0  # backtrack

    return False

def can_color_graph(v, edges, m):
    # Build adjacency list
    graph = [[] for _ in range(v)]
    for u, vtx in edges:
        graph[u].append(vtx)
        graph[vtx].append(u)

    color = [0] * v  # 0 means uncolored
    return solve(0, graph, m, color)
v = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
m = 3
print(can_color_graph(v, edges, m))  # Output: True
