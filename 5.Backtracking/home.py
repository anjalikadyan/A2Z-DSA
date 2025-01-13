from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
#checking row for duplicate number
def check_row(arr, row, num):
    for col in range(9):
        if arr[row][col] == num:
            return False    # Number already exists in row
    return True    # Number is valid for this row
#checking column for duplicate number
def check_col(arr, col, num):
    for row in range(9):
        if arr[row][col] == num:
            return False    # Number already exists in column
    return True    # Number is valid for this column
#checking 3x3 matrix for duplicate number
def matrix(arr, row, col, num):
    startrow = (row // 3) * 3
    startcol = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[startrow + i][startcol + j] == num:
                return False    # Number already exists in 3x3 box
    return True    # Number is valid for this 3x3 box
#checking if the number is valid
def valid(arr, row, col, num):
    return (
        check_row(arr, row, num) and
        check_col(arr, col, num) and
        matrix(arr, row, col, num)
    )
#finding the empty cell
def find_empty(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return i, j
    return None
#main function
def main(arr):
    empty_cell = find_empty(arr)
    if not empty_cell:
        return True      
    row, col = empty_cell
    for num in range(1, 10):
        if valid(arr, row, col, num):
            arr[row][col] = num  
            if main(arr):
                return True  
            arr[row][col] = 0  
    return False  
#printing the grid
def print_grid(arr):
    for i in range(9):
        print(arr[i])
n=9


arr1= [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 4, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# print("Original Sudoku Puzzle:")
# print_grid(arr1)
# print("\nSolution:")
# if main(arr1):
#     print_grid(arr1)
# else:
#     print("No solution exists")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Get the puzzle from the request
        puzzle = request.json['puzzle']
        
        # Convert the puzzle to the correct format (2D list)
        grid = [[int(puzzle[i * 9 + j]) for j in range(9)] for i in range(9)]
        
        # Solve the puzzle
        if main(grid):
            return jsonify({'success': True, 'solution': grid})
        else:
            return jsonify({'success': False, 'message': 'No solution exists'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.debug = True
    app.run()

