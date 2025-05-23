from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    
    # If start or end is blocked, return -1
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1

    # 8-directional movements
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                (0, -1),          (0, 1), 
                (1, -1),  (1, 0),  (1, 1)]

    # BFS queue: (x, y, path_length)
    queue = deque([(0, 0, 1)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y, length = queue.popleft()

        if x == n - 1 and y == n - 1:
            return length

        for dx, dy in directions:
            newX, newY = x + dx, y + dy

            if 0 <= newX < n and 0 <= newY < n and not visited[newX][newY] and grid[newX][newY] == 0:
                visited[newX][newY] = True
                queue.append((newX, newY, length + 1))

    return -1
grid = [
    [0, 1],
    [1, 0]
]

print(shortestPathBinaryMatrix(grid))  # Output: 2
