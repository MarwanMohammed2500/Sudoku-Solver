from helper_functions import *
from generator import *

def get_input():
    user_choice = input("Do you want to input a Sudoku puzzle? (yes/no) ").lower()

    if user_choice == "yes":
        print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
        user_board = []
        for _ in range(9):
            row = [int(num) for num in input().split()]
            user_board.append(row)
        return user_board, None

    elif user_choice == "no":
        difficulty = input("Choose difficulty level: 'easy', 'medium', or 'hard' ").lower()

        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")
        return None, difficulty


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

board, diff = get_input()

if board == None:
    board = generator().generate_board(diff)
else:
    board = np.array(board)
print("\ninitial state: \n")
print_board(board)
print("Solving...\n\n")

sol = solve_sudoku(board)
if sol[0] == False:
    print("Unsolvable!")
else:
    print("Final state:\n")
    print_board(sol[1])
