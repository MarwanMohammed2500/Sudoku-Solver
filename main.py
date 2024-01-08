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
    print("Unsolvable!")
else:
    print("Final state:\n")
    print_board(sol[1])
