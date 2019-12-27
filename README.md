# The BackTracking Algorithm
A very useful and simple algorithm that gives you the capacity to search for all solutions cases to constrain satisfaction problems in a deep first tree way. 

## Description
The BackTracking algorithm allows you to find solutions to constrain satisfaction problems, by incrementally building the solution and then, when it goes into a solutions that doesn't satisfy the constrains it backtracks and experiments other combination, searching the solution space in a deep first tree way. <br>
The BackTracking algorithm in it's simplest form, uses recursion to search for all solutions to a problem. Although you can have early stopping if you find one or some solutions. <br>
In some cases, the validation of each state can be computationally lighter because the solution is built incrementally using the knowledge that the already built solution part is correctly validated. So in some cases, you only have to validate the constrains of what you are adding to the solution in the current step. <br>
Because it is a deep tree first algorithm, normally it uses less memory, than other exhaustive search policies. <br>
Any Backtracking problem has:
1. Choices
2. Constrains
3. Goals

## Pseudocode of the algorithm from wikipedia
1. root(P):     return the partial candidate at the root of the search tree.
2. reject(P,c): return true only if the partial candidate c is not worth completing.
3. accept(P,c): return true if c is a solution of P, and false otherwise.
4. first(P,c):  generate the first extension of candidate c.
5. next(P,s):   generate the next alternative extension of a candidate, after the extension s.
6. output(P,c): use the solution c of P, as appropriate to the application.

```
procedure bt(c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        bt(s)
    s ← next(P, s)

```

Note: For more theoretical details see Wikipedia references in this page.

## Example 1 - Sudoku solver
This is a simple implementation in Python. <br>
In it, we will call the solve() recursive function for each of the empty/zero  positions in the Sudoku given puzzle. The solution will be iteratively constructed from the possible choices and at each step it will be validated against the constrains of the problem. If it satisfy the constrains it will continue to the next empty position and call solve() again. If it finds that the step to the solution isn't valid it will BackTack and try the next possible choice until it find a solution. <br>
When it founds one correct solution it ends the recursion and the solution tree traversal. <br>  
The core of the backtracking algorithm is the following code. <br>

```python
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
        # if valid, incrementally build the next solution phase.
        foundSolutionBoard = solve(row, col, newState)
        if type(foundSolutionBoard) != type(False):
            # Achieved the GOAL.
            return foundSolutionBoard
    return False
```

In backtracking (is iterative), there is a huge time saver. At each point, we know that all the previous solutions have been tested, so we only need to test/validate:
* The current row.
* The current column.
* The current square cell (9 positions).

and not the all board.

For all the details, please see the file [sudoku_solver.py](/sudoku_solver.py) <br> 
<br>
Execution of program...<br>

![Execution of the sudoku solver](/sudoku_solver.png)

## Example 2 - The 8 Queen solver
The 8 Queen problem is the problem of placing 8 chess queens on a 8x8 chess board so that no queen is attacking other queen. <br>
This problem will be solved with backtracking. Iteratively constructing a solution. <br> 
The core of the backtracking algorithm is the following code. <br>

```python
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
```

For all the details, please see the file [the_8_queen_solver.py](/the_8_queen_solver.py) <br> 
<br>
Execution of program for 8x8 chess board, where appear '1' is a Queen. <br>

![A 8x8 chess board](/the_8_queen_puzzle.png)

It can solve in a fast way even for 20 Queens on a 20x20 chess board. <br>

![A 20x20 chess board](/the_20_queen_puzzle.png)


## Example 3 - Sequence generator with constrains
This is a Python program that generates sequences of length N of 3 different elements with the constrain that there cannot be a sequence with with 2 consecutive equal elements. <br>
The problem uses the BackTracking algorithm or strategy. <br>

```python
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
```

For all the details, please see the file [sequence_generator.py](/sequence_generator.py) <br> 
<br>
Execution of program to generate sequences of 4 elements with the constrain that no element can repeat itself consecutively. <br>

![sequence generator 4 elements](/sequence_generator_4_elements.png)

## References
* [Backtracking - Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
* [Video - The Backtracking Blueprint: The Legendary 3 Keys To Backtracking Algorithms](https://www.youtube.com/watch?v=Zq4upTEaQyM)
* [Video - Introduction to Backtracking - Brute Force Approach](https://www.youtube.com/watch?v=DKCbsiDBN6c)
* [Sudoku - Wikipedia](https://en.wikipedia.org/wiki/Sudoku)
* [Implement A Sudoku Solver - Sudoku Solving Backtracking Algorithm](https://www.youtube.com/watch?v=JzONv5kaPJM)
* [Eight queens puzzle - Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
* [The N Queens Placement Problem Clear Explanation Backtracking/Recursion](https://www.youtube.com/watch?v=wGbuCyNpxIg)

## License:
MIT open source

## Have fun!
Best regards, <br>
Joao Nuno Carvalho <br>