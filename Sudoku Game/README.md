# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

In this project, I will be writing code to implement two extensions of the sudoku solver. The first one will be to implement the technique called "naked twins". The second one will be to modify our existing code to solve a diagonal sudoku. To complete this project I will use the tools I learned about in the lesson, and build upon them.

The goals are to implement the naked twins function, and write an AI agent that will solve the Diagonal Sudoku game.

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  

For naked twins, firstly I identify all boxes that have only 2 elements inside. Next, I find the boxes that have the same elements (in order to get the "naked twins"). After that, I remove the corresponding digits from all the boxes that peers with the "twins".
Finally, I add the "naked_twins" in the "reduce_puzzle" function with eliminate and only-choice to reduce the number of possibilities.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  

For diagonal sudoku, I just identify a new unit that represent the two diagonal boxes units in sudoku.
Then, I add the "diagonal units" in the "unitlist" as a condition for constraint propagation. Hence, the solution of the game will satisfy the diagonal constraint.




