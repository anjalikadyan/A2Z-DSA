# Backtracking

**Backtracking** is an algorithmic technique that uses a "try and error" approach to solve problems. It systematically explores all possible solutions to a problem by trying one solution at a time. If a solution does not satisfy the given conditions, the algorithm backtracks (undoes the last step) and tries a different path.

## Key Steps in Backtracking:
1. **Define the Problem:** Clearly specify the problem, including the conditions that must be fulfilled to solve it.
2. **Recursion:** Use recursion to attempt solutions one step at a time.
3. **Undo and Retry:** If the current solution fails to meet the conditions, backtrack by undoing the last step and trying a different option.

Backtracking is useful for problems involving multiple possible conditions or configurations, such as:
- Puzzle solving
- Pathfinding
- Combinatorial problems

---

## Examples

### **1. Solving the N-Queens Problem**
The N-Queens problem requires placing N queens on an N×N chessboard such that no two queens threaten each other (no two queens in the same row, column, or diagonal).

#### **Algorithm:**
1. Place a queen in a row.
2. Check if the position is valid (does not conflict with other queens).
3. If valid, move to the next row and repeat.
4. If no valid position exists, backtrack and try a different position for the previous queen.

#### **Python Implementation:**
```python
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = '.'  # Backtrack

    return False

# Initialize an empty board
N = 4
board = [['.' for _ in range(N)] for _ in range(N)]
solve_n_queens(board, 0, N)
```

**Output:**
```
. Q . .
. . . Q
Q . . .
. . Q .
```

---

### **2. Solving the Maze Problem (Pathfinding)**
Given a maze represented as a grid, the goal is to find a path from the starting position to the destination.

#### **Algorithm:**
1. Start at the initial position.
2. Move to a neighboring cell if it is within bounds and not a wall.
3. If the destination is reached, print the path.
4. If no valid moves exist, backtrack and try a different path.

#### **Python Implementation:**
```python
def is_valid_move(maze, x, y, visited):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and not visited[x][y]

def solve_maze(maze, x, y, path, visited):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:  # Destination reached
        path.append((x, y))
        print("Path:", path)
        return True

    if is_valid_move(maze, x, y, visited):
        visited[x][y] = True
        path.append((x, y))

        # Explore all possible moves
        if solve_maze(maze, x + 1, y, path, visited):
            return True
        if solve_maze(maze, x, y + 1, path, visited):
            return True
        if solve_maze(maze, x - 1, y, path, visited):
            return True
        if solve_maze(maze, x, y - 1, path, visited):
            return True

        # Backtrack
        path.pop()
        visited[x][y] = False

    return False

# Define the maze (1 = path, 0 = wall)
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
path = []

solve_maze(maze, 0, 0, path, visited)
```

**Output:**
```
Path: [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
```

---

### **3. Generating All Subsets of a Set (Combinatorial Problem)**
#### **Algorithm:**
1. Include or exclude each element of the set.
2. Use recursion to generate subsets.
3. Backtrack to remove the last included element and try the next option.

#### **Python Implementation:**
```python
def generate_subsets(nums, index, current, result):
    if index == len(nums):
        result.append(current[:])
        return

    # Include the current element
    current.append(nums[index])
    generate_subsets(nums, index + 1, current, result)

    # Backtrack and exclude the current element
    current.pop()
    generate_subsets(nums, index + 1, current, result)

nums = [1, 2, 3]
result = []
generate_subsets(nums, 0, [], result)
print(result)
```

**Output:**
```
[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
```

