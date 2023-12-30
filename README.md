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






## This program was made possible via the help of @omarjimy who massively contributed to this project, thank you!
