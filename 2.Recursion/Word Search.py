def exist(board, word):
    if not board:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (
            r < 0 or c < 0 or r >= rows or c >= cols
            or board[r][c] != word[i]
        ):
            return False

        # Mark the cell as visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all 4 directions
        found = (
            dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1)
        )

        # Restore the cell
        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCCED"
print(exist(board, word))  # Output: True
