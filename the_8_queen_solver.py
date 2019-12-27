###############################################################################
#                                                                             #
#                         the_8_queen_solver.py                               #
#                                                                             #
###############################################################################
# Author:  Joao Nuno Carvalho                                                 #
# Data:    2019.12.27                                                         #
# License: MIT Open Source License                                            #
#                                                                             #
# Description: This is a Python program to solve the 8 Queen problem puzzle   #
#              using the BackTracking algorithm or strategy.                  #
#              The BackTracking algorithm is a way of solving constrained     #
#              satisfiable problems using recursion in a deep first tree      #
# traversal, in witch the solution is found iteratively. When the constrains  #
# aren't satisfied the solution step is backtracked, and from that comes it's #
# name. It founds the first solution and exits.                               #
# It can solve in a fast way even for 20 queens on a 20x20 chess board.       #
# Any Backtracking problem has:                                               #
#    -Choices                                                                 #
#    -Constrains                                                              #
#    -Goals                                                                   #
#                                                                             #
# To Run this code do:                                                        #
#                      Python the_8_queen_solver.py                           #
#                                                                             #
# For references see the project page at:                                     #
#     https://github.com/joaocarvalhoopen?tab=repositories                    #
###############################################################################  

import numpy as np

MAX_NUM_ROWS = 8 # 20
MAX_NUM_COLS = 8 # 20

def printBoard(state, message):
    print("\n" + message + "\n")
    for row in range(0, MAX_NUM_ROWS):
        for col in range(0, MAX_NUM_COLS):
            print(state[row][col], end='')
            if col == MAX_NUM_COLS-1:
                print()
            else:
                print(" ", end='')

def isBoardStateConstrainsSatisfied(row_in, col_in, state):
    # Check the constrains. 
    # Because we are building the solution iteratively, and the previous boards with
    # the previous placed queens are correct and not attacking each other, we only
    # need to check if there is a queen:
    #   -in the some row, 
    #   -in the same column,
    #   -and in a diagonal of our current position.  

    # Check row. 
    for col in range(0, MAX_NUM_COLS):
        if col == col_in:
            continue
        if state[row_in][col] == 1:
            return False

    # Check column.
    for row in range(0, MAX_NUM_ROWS):
        if row == row_in:
            continue
        if state[row][col_in] == 1:
            return False

    # Check diagonals upper left.
    row = row_in
    col = col_in 
    while (True):
        row -= 1
        col -= 1
        if row >= 0 and col >= 0:
            if state[row, col] == 1:
                return False
        else:
            break         

    # Check diagonals upper right.
    row = row_in
    col = col_in 
    while (True):
        row -= 1
        col += 1
        if row >= 0 and col < MAX_NUM_COLS:
            if state[row, col] == 1:
                return False
        else:
            break         

    # Check diagonals down left.
    row = row_in
    col = col_in 
    while (True):
        row += 1
        col -= 1
        if row < MAX_NUM_ROWS and col >= 0:
            if state[row, col] == 1:
                return False
        else:
            break         

    # Check diagonals down right.
    row = row_in
    col = col_in 
    while (True):
        row += 1
        col += 1
        if row < MAX_NUM_ROWS and col < MAX_NUM_COLS:
            if state[row, col] == 1:
                return False
        else:
            break         

    # NOTE: We can implement in a simpler way, testing all board position, it can
    #       also work for a small board of 8x8, but that would not work but a bigger board.
    #
    #for row in range(0, MAX_NUM_ROWS):
    #    for col in range(0, MAX_NUM_COLS):
    #        rowDiff = row - row_in
    #        colDiff = col - col_in  
    #        if not (row == row_in and col == col_in) and 
    #           (row == row_in or col == col_in or rowDiff == colDiff))
    #           if state[row][col]] == 1:
    #               return False    

    return True


def solve(row_in, col_in, state):
    # Establish the stopping GOAL. 
    if row_in >= MAX_NUM_ROWS:
        return state.copy()

    # Give all the CHOICES to experiment incrementally.
    newState = state.copy()
    for choice in range(0, MAX_NUM_COLS):
        col = choice
        newState[row_in, col] = 1
        # Validate choice against CONSTRAINS.
        if not isBoardStateConstrainsSatisfied(row_in, col, newState):
            # Removes the previous choice.
            newState[row_in, col] = 0
            continue
        # if valid, incrementally build the next solution phase.
        foundSolutionBoard = solve(row_in + 1, col, newState)
        if type(foundSolutionBoard) != type(False):
            # Achieved the GOAL.
            return foundSolutionBoard
        # Removes the previous choice.
        newState[row_in, col] = 0    
    return False

if __name__ == "__main__":
    print("\n#############################")
    print(  "# The 8 Queen Puzzle Solver #")
    print(  "#############################")

    board = np.zeros((MAX_NUM_ROWS, MAX_NUM_COLS), dtype='int')
    printBoard(board, "Puzzle board...")
    row = 0
    col = 0
    foundSolutionBoard = solve(row, col, board)
    printBoard(foundSolutionBoard, "Solution...")

