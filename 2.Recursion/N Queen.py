def solveNQueens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def backtrack(row):
        if row == n:
            board = []
            for i in range(n):
                row_str = ['.'] * n
                row_str[queens[i]] = 'Q'
                board.append("".join(row_str))
            solutions.append(board)
            return

        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # Undo the move
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

    solutions = []
    queens = [-1] * n
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    backtrack(0)
    return solutions
n = 4
result = solveNQueens(n)
for board in result:
    for row in board:
        print(row)
    print()
