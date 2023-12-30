from game_generator import *

def solver(board):
    full = is_full(board)
    valid = True
    
    if not full:
        row, col = find_empty_cell(board)
        if row == None:
            return board

        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                valid = True
                solver(board)
                # break
            else:
                valid = False
    if not valid:
        board[row][col] = 0 



board = generate_puzzle()
print(solver(board))
print("Done!")
# print(solved)
