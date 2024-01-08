import numpy as np

def print_board(board): # Prints out the sudoku board
    itr = 0
    for row in board:
        itr += 1
        print("|", " ".join(map(str, row)), "|")

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
