from helper_functions import *
import random

class generator():
    def __init__(self):
        self.board = np.zeros((9, 9), np.uint16) # Generates a board of zeros
        
    def generate_board(self, difficulty = "hard"):
        count = 0 # --> To count how many iterations have been done.
        available_nums = np.array([i for i in range(1, 10)]) # --> Available numbers in each row
        random.shuffle(available_nums) # --> Shuffles them randomly to create some randomness in the creation of puzzle, so each puzzle generated is different
        
        while True: # --> Loops, using backtracking (or DFS Teqnique) to generate the board
            row, col = find_empty_cell(self.board) # --> Finds the first empty cell
            if row == None: # --> If the board is full
                break
            if count > 81: # --> if it iterated more than 81 times over a singular board, it means it's incorrect, so it breaks and tries a different one.
                break
            
            for num in available_nums: # --> Loops over the available numbers, checking if it's valid to put that number in that cell
                if is_valid(self.board, row, col, num):
                    available_nums = np.delete(available_nums, np.where(available_nums == num))
                    self.board[row][col] = num
                    
                    break
            
            if (self.board[row][col] == 0): # --> if a cell is still empty, then try to switch it with a previous one if valid.
                for j in available_nums:
                    for i in range(1, col+1):
                        tmp = self.board[row][col - i]
                        self.board[row][col - i] = 0
                        if (is_valid(self.board, row, col, tmp)) and (is_valid(self.board, row, col - i, j)):
                            self.board[row][col] = tmp
                            self.board[row][col - i] = j
                            available_nums = np.delete(available_nums, np.where(available_nums == j))
                            
                            break
                        else:
                            self.board[row][col - i] = tmp
                    if self.board[row][col] != 0:
                        break

            if (col == 8) and (self.board[row][col] != 0): # resets the available numbers to insert in a row if we move onto a new row.
                available_nums = np.array([i for i in range(1, 10)])
                random.shuffle(available_nums)
            count += 1 # --> to indicate a finished iteration
        
        if count > 82: # --> if it reaches 82, then it recursevely tries to generate a new board, the reason it is 82, is because a sudoku board will be generated (in the worst case scenario) after 81 iterations, and i gave it one more iteration for the hell of it tbh, after that, it doesn't make sense, so, try with a new board
            self.board = np.zeros((9, 9), np.uint16)
            return self.generate_board()
        
        if difficulty == "easy":
            cells_to_remove = 40
        elif difficulty == "medium":
            cells_to_remove = 50
        elif difficulty == "hard":
            cells_to_remove = 60
        else:
            raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")
        cells = [(i, j) for i in range(9) for j in range(9)]
        np.random.shuffle(cells)

        for i, j in cells[:cells_to_remove]: # --> removes a cell, checking if it still generates a unique board afterwards.
            backup = self.board[i][j]
            self.board[i][j] = 0

            # check if the solution is still unique
            if not self.unique(i, j, backup):
                self.board[i][j] = backup

        # print(self.board)
        return self.board

    def unique(self, row, col, original): # Checks if the board is still unique after removing a specific cell.
        # copy the board and check if the puzzle has a unique solution
        temp = self.board
        for num in range(1, 10):
            if is_valid(temp, row, col, num):
                if num != original:
                    return False
        return True
