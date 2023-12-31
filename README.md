# This script generates an unsoved sudoku board, then goes and solves it

The way it does that is by:
  1) Finding the first empty cell (the cell containing a zero, starting from index (0, 0) and ending at (8, 8)).
  2) It then goes on trying number from 1 to 9 in that cell, checking if the number is valid in that position or not (following the sudoku rules).
  3) If the number is valid it puts it in that position, if not it tries anothe one
  4) if all 9 numbers are invalid in that position, then it goes back to the position right before it and tries other numbers in it, if non works on that as well, it empties that position, and then tries again with the one before that.
  5) It keeps doing that till the entire board is solved


Stuff to be added in future versions:
  1) The ability to add your own board for the program to solve for you,
  2) It stops iterating over the board trying to solve it after 500-600 iterations, that means it's unsolvable.
  3) print out the board without printing out an error instead.


## helper_functions.py:
This script containts all the functions that are fundemental for either generating the puzzle or solving it.
  1) print_board:
       - Prints the board, **returns None**
  2) is_valid:
       - Checks the validity of the number to insert in a specific cell, **returns bool**
  3) find_empty_cell:
       - Finds and returns the first empty cell it encounters, **returns tuple**
  4) is_full:
       - Checks if the board it full, **return bool**

## generator.py:
This script is responsible for the generation of the puzzle, it does so by generating a full, and valid sudoku board, then it randomly removes elements from it after making sure it still will give us a unique solution.
  1) solve_sudoku:
       - Responsible of generating a full board, making sure it is valid and then returns a boolean value indicating a successful or failed generation, **returns bool**
  2) generate:
       - Generates the puzzle, it removes random values from the board, while still making sure it is unique and valid, **returns np.array**
  3) unique:
       - Makes sure that a specific cell can hold one and only one value after the full generation of the board, **returns bool**


## game.py:
This is the actual model that solves the game, it uses a backtracking (DFS) algorthim to solve the board
  1) solver:
       - Solves the board using backtracking teqnique, **return np.array**

## This program was made possible via the **MASSIVE** help of @omarjimy who massively contributed to this project, thank you!
