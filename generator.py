from helper_functions import *
class generator():
    def __init__(self):
        self.board = np.zeros((9, 9), np.uint16) # Generates a board of zeros
        
    def solve_sudoku(self, board):
        row, col = find_empty_cell(self.board)

        # no empty cells (solved)
        if row is None:
            return True

        # try a random value first and see if it is valid
        # val = np.random.randint(1, 10)
        # if is_valid(self.board, row, col, val):
        #         self.board[row][col] = val
        #         if self.solve_sudoku(self.board):
        #                 return True
        # if not, try other numbers between 1 and 9
        # else:
        # try each number 1 to 9
        for num in range(1, 10):
            if is_valid(self.board, row, col, num):
                self.board[row][col] = num

                # recursively try to solve the rest
                if self.solve_sudoku(self.board):
                    return True

                # does not lead to a solution, backtrack
                self.board[row][col] = 0

        # no solution (invalid table)
        return False
    
    
    def generate(self):
        # generates a complete Sudoku board
        self.solve_sudoku(self.board)
        
        # if difficulty == "easy":
        #     cells_to_remove = 40
        # elif difficulty == "medium":
        #     cells_to_remove = 50
        # elif difficulty == "hard":
        #     cells_to_remove = 60
        # else:
        #     raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")

        # randomly remove cells based on the difficulty level
        cells = [(i, j) for i in range(9) for j in range(9)]
        np.random.shuffle(cells)

        for i, j in cells[:60]:
            backup = self.board[i][j]
            self.board[i][j] = 0

            # check if the solution is still unique
            if not self.unique(i, j, backup):
                self.board[i][j] = backup

        return self.board

    def unique(self, row, col, original):
        # copy the board and check if the puzzle has a unique solution
        temp = self.board
        for num in range(1, 10):
            if is_valid(temp, row, col, num):
                if num != original:
                    return False
        return True
    
# g = generator()
# board = g.generate()
# print("\n\n", board)