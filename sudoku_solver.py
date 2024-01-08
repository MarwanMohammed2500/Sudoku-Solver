from helper_functions import *
from generator import *

def solve_sudoku(board): # --> Solves the sudoku puzzle
    row, col = find_empty_cell(board) # --> finds the first empty cell.

    # no empty cells (solveed)
    if row is None: # --> checks if the board is full.
        return (True, board)

    # try each number 1 to 9
    for num in range(1, 10): # --> iterates over the possible values for a specific cell.
        if is_valid(board, row, col, num):
            board[row][col] = num

            # recursively try to solve the rest
            if solve_sudoku(board)[0]:
                return (True, board)

            # does not lead to a solution, backtrack
            board[row][col] = 0

    # no solution (invalid table)
    return (False, False)
