###############################################################################
#                                                                             #
#                      Sequence generator with constrains                     #
#                                                                             #
###############################################################################
# Author:  Joao Nuno Carvalho                                                 #
# Data:    2019.12.27                                                         #
# License: MIT Open Source License                                            #
#                                                                             #
# Description: This is a Python program that generates sequences of length N  #
#              of 3 different elements with the constrain that there cannot   #
#              be a sequence with with 2 consecutive equal elements.          #
#              The problem uses the BackTracking algorithm or strategy.       #
#              The BackTracking algorithm is a way of solving constrained     #
#              satisfiable problems using recursion in a deep first tree      #
# traversal, in witch the solution is found iteratively. When the constrains  #
# aren't satisfied the solution step is backtracked, and from that comes it's #
# name. It founds the first solution and exits.                               #
# Any Backtracking problem has:                                               #
#    -Choices                                                                 #
#    -Constrains                                                              #
#    -Goals                                                                   #
#                                                                             #
# To Run this code do:                                                        #
#                      Python sequence_generator.py                           #
#                                                                             #
# For references see the project page at:                                     #
#     https://github.com/joaocarvalhoopen?tab=repositories                    #
###############################################################################  

import numpy as np

MAX_SEQUENCE_LENGTH = 4
SEQUENCE_ELEMENTS = ['A', 'B', 'C']

def printSequences(state, message):
    print("\n" + message + "\n")
    for seq in state:
        for i in range(0, MAX_SEQUENCE_LENGTH):
            print(seq[i], end='')
            if i == MAX_SEQUENCE_LENGTH-1:
                    print()

def isSequenceStateConstrainsSatisfied(index, state):
    # Check the constrains. 
    # Because we are building the solution iteratively, and the previous state with
    # the previous sequence is correct and not conflicting, we only
    # need to check if there current value is:
    #   -not equal to the previous value.  

    # Check if not equal to previous value.
    if (index > 0):
        if state[index - 1] == state[index]:
            return False  
    
    return True

def solve(index_in, state, allSequenceSolution):
    # Establish the stopping GOAL. 
    if index_in >= MAX_SEQUENCE_LENGTH:
        allSequenceSolution.append(state.copy())
        return True

    # Give all the CHOICES to experiment incrementally.
    newState = state.copy()
    for choice in SEQUENCE_ELEMENTS:
        newState[index_in] = choice
        # Validate choice against CONSTRAINS.
        if not isSequenceStateConstrainsSatisfied(index_in, newState):
            # Removes the previous choice.
            newState[index_in] = '_'
            continue
        # if valid, incrementally build the next solution phase.
        solve(index_in + 1, newState, allSequenceSolution)
        # Removes the previous choice.
        newState[index_in] = '_'

if __name__ == "__main__":
    print("\n######################################")
    print(  "# Sequence generator with constrains #")
    print(  "######################################")

    # The '_' mark the places where we will put a sequence element! 
    sequenceLst = []
    for i in range(0, MAX_SEQUENCE_LENGTH):
        sequenceLst.append('_')

    sequence = np.array(sequenceLst)
    printSequences([sequence], "Empty sequence...")
    index = 0
    allSequenceSolution = []
    solve(index, sequence, allSequenceSolution)
    printSequences(allSequenceSolution, "All valid sequences...")

