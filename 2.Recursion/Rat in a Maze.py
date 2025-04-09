def find_paths(mat):
    n = len(mat)
    result = []

    # Check if the source is blocked
    if mat[0][0] == 0 or mat[n - 1][n - 1] == 0:
        return result

    # Directions: D, L, R, U (in lexicographic order)
    directions = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}

    def is_safe(x, y, visited):
        return 0 <= x < n and 0 <= y < n and mat[x][y] == 1 and not visited[x][y]

    def backtrack(x, y, path, visited):
        if x == n - 1 and y == n - 1:
            result.append(path)
            return

        for move in sorted(directions):  # Ensure lexicographical order
            dx, dy = directions[move]
            new_x, new_y = x + dx, y + dy

            if is_safe(new_x, new_y, visited):
                visited[new_x][new_y] = True
                backtrack(new_x, new_y, path + move, visited)
                visited[new_x][new_y] = False  # Backtrack

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    backtrack(0, 0, "", visited)

    return result
mat = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

paths = find_paths(mat)
print(paths)
