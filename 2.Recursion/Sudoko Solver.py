def solve_sudoku(board):
    from collections import defaultdict

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty_cells = []

    # Initialize tracking sets
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                empty_cells.append((r, c))
            else:
                num = board[r][c]
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3) * 3 + (c // 3)].add(num)

    def backtrack(i=0):
        if i == len(empty_cells):
            return True  # All cells filled

        r, c = empty_cells[i]
        box_index = (r // 3) * 3 + (c // 3)

        for num in '123456789':
            if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

                if backtrack(i + 1):
                    return True

                # Undo on backtrack
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_index].remove(num)

        return False

    backtrack()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)

for row in board:
    print(row)
