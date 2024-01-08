from helper_functions import *
from generator import *
from sudoku_solver import *

def main():
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
    return "Unsolvable!"
else:
    print("Final state:\n")
    return sol[1]

if __name__ == "__main__":
  print(main())
