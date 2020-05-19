"""
James Yang
Summer 2020 Sudoku Solver Project
Backtracking Algorithm
"""

# function to make console print more visually appealing. Simply prints dividers like a normal sudoku board
def print_grid(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" |  ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# function checks and returns the position of empty spots on the board
def empty_spot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # (y, x)
    return None


def valid_loc(location, value, board):
    # checks the column
    for i in range(len(board[0])):
        if board[i][location[1]] == value and location[0] != i:
            return False
    # checks the row
    for j in range(len(board)):
        if board[location[0]][j] == value and location[1] != j:
            return False

    # checks square
    x = location[1] // 3  # finds index of the square relative to grid
    y = location[0] // 3  # finds y

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == value and [i, j] != location:
                return False
    return True


# recursive backtracking solution
def backtracking(board):
    coordinates = empty_spot(board)
    if not coordinates:
        return True
    else:
        y, x = coordinates

    for i in range(1, 10): # checking numbers 1 - 9 (10 is not inclusive)
        if valid_loc([y, x], i, board):
            board[y][x] = i

            if backtracking(board):
                return True

            # if backtracking(board) is false, it will backtrack and reset the location's value to 0
            board[y][x] = 0

    return False


sample_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
# empty board for user to fill in if they want to solve a puzzle
new_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

backtracking(sample_board)
print_grid(sample_board)


