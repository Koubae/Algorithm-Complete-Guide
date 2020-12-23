Backtraking
========

Backtracking is a **recursive** Algorithm that try all possible possibilities, it uses to solve Puzzles, Mazes, crosswords, Sudoku etc.., is finding the solution of a problem whereby *the solution depends on the previous steps taken.*

Typical problems
----------------

* The Knight’s tour problem

> Python

> C

--------------------------

* Path followed by Knight to cover all the cells

* Rat in a maze.

* Sudoku



Documentation
-------------

You must first understand how **Recursive programming** works!


In backtracking, we first start with a partial sub-solution of the problem (which may or may not lead us to the solution) and then check if we can proceed further with this sub-solution or not. If not, then we just come back and change it.

General steps:

1. Start with a sub-solution.

2. Check if this sub-solution will lead to the solution or not.

3. If not, then come back and change the sub-solution and loop recursevely until you find the solution.

### Rat in a maze

- Python

- C

- Java

The Start Position is always the Top-left corner, the Destination The Right Bottom Corner.



How we approach the problem:

1. Check for the current cell, if it is the destination cell, then the puzzle is solved.

2. If not, then we will try to move downward and see if we can move in the downward cell or not (to move in a cell it must be vacant and not already present in the path).

3. If we can move there, then we will continue with the path taken to the next downward cell.
If not, we will try to move to the rightward cell. And if it is blocked or taken, we will move upward.
Similarly, if we can't move up as well, we will simply move to the left cell.

4. If none of the four moves (down, right, up, or left) are possible, we will simply move back and change our current path (backtracking).

-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------



-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------

* Subsets

* Combinations

* Permutations


-----------------------------------------------------------------------------------------------------

References
----------



-----------------------------------------------------------------------------------------------------

Notes
-----