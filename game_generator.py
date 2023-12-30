import numpy as np

def print_board(board): # Prints out the sudoku board
    for row in board:
        print("|".join(map(str, row)))
    
    

def is_valid(board, row, col, num): # Checks if a number is valid in a specific cell
    # check if 'num' is not in the same row, column, or subgrid
    return (
        all(num != board[row][i] for i in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] for i in range(9))
    )

def find_empty_cell(board): # Returns the first empty cell it encounters
    # find the first empty cell (0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    
    return None, None

def is_full(board): # Checks if the board is full or not
    if len(board[board == 0]) > 0:
        return False
    else:
        return True


def generate_puzzle(): # Generates a puzzle
    board = np.zeros((9, 9), np.uint16)
    row, col = (np.random.randint(9), np.random.randint(9))
    board[row][col] = np.random.randint(1, 10)
    for i in range(20):
        r, c = (np.random.randint(9), np.random.randint(9))
        val = np.random.randint(1, 10)
        if is_valid(board, r, c, val) and (board[r][c]) == 0:
            board[r][c] = val
    return board

# board = generate_puzzle()
# print(board)
# print(is_full(board))
# print(find_empty_cell(board))
