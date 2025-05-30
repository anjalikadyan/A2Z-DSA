from collections import deque

def updateMatrix(mat):
    if not mat:
        return []

    rows, cols = len(mat), len(mat[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if 0 <= newX < rows and 0 <= newY < cols:
                if dist[newX][newY] > dist[x][y] + 1:
                    dist[newX][newY] = dist[x][y] + 1
                    queue.append((newX, newY))

    return dist
mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

result = updateMatrix(mat)
for row in result:
    print(row)
