###############################################################################
#                                                                             #
#                             sudoku_solver.py                                #
#                                                                             #
###############################################################################
# Author:  Joao Nuno Carvalho                                                 #
# Data:    2019.12.27                                                         #
# License: MIT Open Source License                                            #
#                                                                             #
# Description: This is a Python program to solve Sudoku Puzzles using the     #
#              BackTracking algorithm or strategy.                            #
#              The BackTracking algorithm is a way of solving constrained     #
#              satisfiable problems using recursion in a deep first tree      #
# traversal, in witch the solution is found iteratively. When the constrains  #
# aren't satisfied the solution step is backtracked, and from that comes it's #
# name. Each board position calls the solve() function.                       #
# Any Backtracking problem has:                                               #
#    -Choices                                                                 #
#    -Constrains                                                              #
#    -Goals                                                                   #
#                                                                             #
# To Run this code do:                                                        #
#                      1. Change your Sudoku empty puzzle.                    #
#                      2. Python sudoku.py                                    #
#                                                                             #
# For references see the project page at:                                     #
#     https://github.com/joaocarvalhoopen?tab=repositories                    #
###############################################################################  

import numpy as np

MAX_NUM_ROWS = 9
MAX_NUM_COLS = 9
EMPTY_LIST = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
START_SQUARE_PAIRS = [(0, 0), (0, 3), (0, 6),
                      (3, 0), (3, 3), (3, 6),
                      (6, 0), (6, 3), (6, 6)]

def printBoard(state, message):
    print("\n" + message + "\n")
    for row in range(0, MAX_NUM_ROWS):
        for col in range(0, MAX_NUM_COLS):
            print(state[row][col], end='')
            if col == MAX_NUM_COLS-1:
                print()
            else:
                print(" ", end='')
                if col == 2 or col == 5:
                    print(" ", end='')
        if row == 2 or row == 5:
            print("")

def getNextValidBoardPos(row_in, col_in, state):
    for row in range(row_in, MAX_NUM_ROWS):
        for col in range(col_in, MAX_NUM_COLS):
            if state[row, col] == 0:
                return row, col
        col_in = 0
    return None, None

def isBoardStateConstrainsSatisfied(state):
    # Constrains:
    
    # In each line can only have one number of the possible ones from 1 to 9.
    for row in range(0, MAX_NUM_ROWS):
        numLst = EMPTY_LIST.copy()
        for col in range(0, MAX_NUM_COLS):
            numLst[state[row, col]] += 1
        if max(numLst[1: ]) > 1:
            return False

    # In each column can only have one number of the possible ones from 1 to 9.
    for col in range(0, MAX_NUM_COLS):
        numLst = EMPTY_LIST.copy()
        for row in range(0, MAX_NUM_ROWS):
            numLst[state[row, col]] += 1
        if max(numLst[1: ]) > 1:
            return False

    # Search in each square.
    for startPair in START_SQUARE_PAIRS:
        row, col = startPair 
        numLst = EMPTY_LIST.copy()
        numLst[state[row,   col]]   += 1
        numLst[state[row,   col+1]] += 1
        numLst[state[row,   col+2]] += 1
        numLst[state[row+1, col]]   += 1
        numLst[state[row+1, col+1]] += 1
        numLst[state[row+1, col+2]] += 1
        numLst[state[row+2, col]]   += 1
        numLst[state[row+2, col+1]] += 1
        numLst[state[row+2, col+2]] += 1
        if max(numLst[1: ]) > 1:
            return False

    # All the board constrains are satisfied.
    return True

def isIterativeBoardStateConstrainsSatisfied(row_in, col_in, state):
    # In backtracking (iterative version), we know that all the previous
    # solutions have been tested, so we only need to test/validate:
    #    -The current row.
    #    -The current column.
    #    -The current square cell (9 positions)
    # This is a huge time saver. 
    
    # Constrains:
    
    # For the current row, test if each position as one number of the possible ones from 1 to 9.
    numLst = EMPTY_LIST.copy()
    for col in range(0, MAX_NUM_COLS):
        numLst[state[row_in, col]] += 1
    if max(numLst[1: ]) > 1:
        return False

    # For the current row, test if each position as one number of the possible ones from 1 to 9.
    numLst = EMPTY_LIST.copy()
    for row in range(0, MAX_NUM_ROWS):
        numLst[state[row, col_in]] += 1
    if max(numLst[1: ]) > 1:
        return False

    # Search in each square.
    for startPair in START_SQUARE_PAIRS:
        r, c = startPair 
        if  not ((r <= row_in < r + 3) and (c <= col_in < c + 3)):
            continue
        numLst = EMPTY_LIST.copy()
        numLst[state[r,     c]]     += 1
        numLst[state[r,     c + 1]] += 1
        numLst[state[r,     c + 2]] += 1
        numLst[state[r + 1, c]]     += 1
        numLst[state[r + 1, c + 1]] += 1
        numLst[state[r + 1, c + 2]] += 1
        numLst[state[r + 2, c]]     += 1
        numLst[state[r + 2, c + 1]] += 1
        numLst[state[r + 2, c + 2]] += 1
        if max(numLst[1: ]) > 1:
            return False

    # All the board constrains are satisfied.
    return True


def solve(row_in, col_in, state):
    # Skip to valid board positions that have a zero (empty position).
    row, col = getNextValidBoardPos(row_in, col_in, state)
    # Test if achieved the GOAL, end the search return the solution board.
    if row == None:
        return state.copy()
    # Give all the CHOICES to experiment incrementally.
    newState = state.copy()
    for choice in range(1, 10):
        newState[row, col] = choice
        # Validate choice against CONSTRAINS.
        if not isIterativeBoardStateConstrainsSatisfied(row, col, newState):
            continue
        # if not isBoardStateConstrainsSatisfied(newState):
        #    continue
        
        # if valid, incrementally build the next solution phase.
        foundSolutionBoard = solve(row, col, newState)
        if type(foundSolutionBoard) != type(False):
            # Achieved the GOAL.
            return foundSolutionBoard
    return False

if __name__ == "__main__":
    print("\n########################")
    print(  "# Sudoku Puzzle Solver #")
    print(  "########################")

    # The Zeros mark the places where we will have to discover the number! 
    sudoku_to_solve = [[ 5, 3, 0,  0, 7, 0,  0, 0, 0],
                       [ 6, 0, 0,  1, 9, 5,  0, 0, 0],
                       [ 0, 9, 8,  0, 0, 0,  0, 6, 0],

                       [ 8, 0, 0,  0, 6, 0,  0, 0, 3],
                       [ 4, 0, 0,  8, 0, 3,  0, 0, 1],
                       [ 7, 0, 0,  0, 2, 0,  0, 0, 6],

                       [ 0, 6, 0,  0, 0, 0,  2, 8, 0],
                       [ 0, 0, 0,  4, 1, 9,  0, 0, 5],
                       [ 0, 0, 0,  0, 8, 0,  0, 7, 9]]
    
    board = np.array(sudoku_to_solve)
    printBoard(board, "Puzzle board...")
    row = 0
    col = 0
    foundSolutionBoard = solve(row, col, board)
    printBoard(foundSolutionBoard, "Solution...")


