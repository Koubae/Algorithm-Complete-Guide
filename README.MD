Algorithms
========


Computer science is the study of problems, problem-solving, and the solutions that come out of the problem-solving process. Given a problem, a computer scientist’s goal is to develop an algorithm, a step-by-step list of instructions for solving any instance of the problem that might arise. Algorithms are finite processes that if followed will solve the problem. Algorithms are solutions.[ref](#Gerry_Jenkins)


-----------------------------------------------------------------------------------------------------

Documentation
-------------


* Search 
* Insertion
* Deletion
* Spare Required
* Time Complexity


### Recursion


All recursive algorithms must obey three important laws:

- A recursive algorithm must have a base case.

- A recursive algorithm must change its state and move toward the base case.

- A recursive algorithm must call itself, recursively.


**Base case** is the condition that allows the algorithm to stop recursing.

**Change of state** means that some data that the algorithm is using is modified. Usually the data that represents our problem gets smaller in some way.



### Design Techniques

Selecting a proper designing technique for a parallel algorithm is the most difficult and important task. Most of the parallel programming problems may have more than one solution. In this chapter, we will discuss the following designing techniques for parallel algorithms −

- Divide and conquer
- Greedy Method
- Dynamic Programming
- Backtracking
- Branch & Bound
- Linear Programming


#### Divide and Conquer Method

In the divide and conquer approach, the problem is divided into several small sub-problems. Then the sub-problems are solved recursively and combined to get the solution of the original problem.

The divide and conquer approach involves the following steps at each level −

- Divide − The original problem is divided into sub-problems.

- Conquer − The sub-problems are solved recursively.

- Combine − The solutions of the sub-problems are combined together to get the solution of the original problem.

The divide and conquer approach is applied in the following algorithms −

- Binary search
- Quick sort
- Merge sort
- Integer multiplication
- Matrix inversion
- Matrix multiplication


#### Greedy Method

In greedy algorithm of optimizing solution, the best solution is chosen at any moment. A greedy algorithm is very easy to apply to complex problems. It decides which step will provide the most accurate solution in the next step.

This algorithm is a called greedy because when the optimal solution to the smaller instance is provided, the algorithm does not consider the total program as a whole. Once a solution is considered, the greedy algorithm never considers the same solution again.

A greedy algorithm works recursively creating a group of objects from the smallest possible component parts. Recursion is a procedure to solve a problem in which the solution to a specific problem is dependent on the solution of the smaller instance of that problem.


#### Dynamic programming 

Is an optimization technique, which divides the problem into smaller sub-problems and after solving each sub-problem, dynamic programming combines all the solutions to get ultimate solution. Unlike divide and conquer method, dynamic programming reuses the solution to the sub-problems many times.


#### Recursive algorithm 

for Fibonacci Series is an example of dynamic programming.


#### Backtracking Algorithm

Backtracking is an optimization technique to solve combinational problems. It is applied to both programmatic and real-life problems. Eight queen problem, Sudoku puzzle and going through a maze are popular examples where backtracking algorithm is used.

In backtracking, we start with a possible solution, which satisfies all the required conditions. Then we move to the next level and if that level does not produce a satisfactory solution, we return one level back and start with a new option.


#### Branch and Bound

Branch and bound algorithm  Is an optimization technique to get an optimal solution to the problem. It looks for the best solution for a given problem in the entire space of the solution. The bounds in the function to be optimized are merged with the value of the latest best solution. It allows the algorithm to find parts of the solution space completely.

The purpose of a branch and bound search is to maintain the lowest-cost path to a target. Once a solution is found, it can keep improving the solution. Branch and bound search is implemented in depth-bounded search and depth–first search.


#### Linear Programming

Linear programming describes a wide class of optimization job where both the optimization criterion and the constraints are linear functions. It is a technique to get the best outcome like maximum profit, shortest path, or lowest cost.

In this programming, we have a set of variables and we have to assign absolute values to them to satisfy a set of linear equations and to maximize or minimize a given linear objective function.

### Time Complexity


#### Linear

- Linear **O(n)**

#### Sublinear 

- [Logarithmic](https://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly) (Binary Search) **O(log n) | O(ln n)**
- Quasilinear **O(n log n)**

- Constant **O(1)** | Constant Time 
- Quadratic **O(n²)**
- Cubic **O(n³)**
- Polynomial Runtime **O(n^k)** **O(n^2)**
- Exponential **O(Xⁿ)**
- Factorial/Combinatorial **O(n!)**


#### Time Complexity - Big O Notaction 

Table in order from best to worst

| Name         | Notation      |
|--------------|---------------|
| Constant     | O(1)          |
| Logarithm    | O(log n)      |
| Linear       | O(n)          | 
| Quasilinear  | O(n log n)    |
| Quadratic    | O(n²)         |
| Cubic        | O(n³)         | 
| Polynomial   | O(n^k)        | 
| Exponential  | O(Xⁿ) / O(2ⁿ) | 
| Factorial    | O(n!)         | 

-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------


- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)

- [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

- [Induced path | induced cycle | chordless cycles](https://en.wikipedia.org/wiki/Induced_path)

- [Chordless Cycle](https://mathworld.wolfram.com/ChordlessCycle.html)

- [Full-text search --WIKI--](https://en.wikipedia.org/wiki/Full-text_search)

- [Approximate string matching --WIKI--](https://en.wikipedia.org/wiki/Approximate_string_matching)

- [Avalanche effect](https://en.wikipedia.org/wiki/Avalanche_effect)

- in-place or in-situ, algorithms.

* [What Should You Learn First: Data Structures or Algorithms?](https://www.geeksforgeeks.org/what-should-i-learn-first-data-structures-or-algorithms/#:~:text=With%20all%20the%20cases%20put,without%20the%20knowledge%20of%20Algorithms.)
**Quick answer: ** _Data Structure basic then Algorithms and keep study Data structure in the same time_


* [Algorithms and Data Structures Cheatsheet | In Java](https://algs4.cs.princeton.edu/cheatsheet/)

-----------------------------------------------------------------------------------------------------


Visualizations
---------------

* [visualgo](https://visualgo.net/en/list)
* [codelike.in | linked-list](https://www.codelike.in/animation/linked-list)
* [Bredth-First Search Visualization](https://www.cs.usfca.edu/~galles/visualization/BFS.html)

-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------

- Time Complexity
- Space Complexity (pc space consumption)

- Best-case complexity − When the amount of time required by an algorithm for a given input is minimum.
- Worst-case complexity − When the amount of time required by an algorithm for a given input is maximum.
- Average-case complexity − When the amount of time required by an algorithm for a given input is average.
- Asymptotic Analysis:
The complexity or efficiency of an algorithm is the number of steps executed by the algorithm to get the desired output. 
Asymptotic notation is the easiest way to describe the fastest and slowest possible execution time for an algorithm using high bounds and low bounds on speed. For this, we use the following notations:


- **Big O notation**
- **Omega notation**
- **Theta notation**
- Speedup of an Algorithm
- Total Cost
- Avalanche effect
- [Space–time tradeoff](https://en.wikipedia.org/wiki/Space%E2%80%93time_tradeoff)
- [Bisection method](https://en.wikipedia.org/wiki/Bisection_method)
- [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function)
- in-place or in-situ, algorithms.
- asymptotic complexity

- Abstract data type  
  - [ADT](https://en.wikipedia.org/wiki/Abstract_data_type#:~:text=In%20computer%20science%2C%20an%20abstract,the%20behavior%20of%20these%20operations.)
  - [ADT | geeksforgeeks](https://www.geeksforgeeks.org/abstract-data-types/)
- data abstraction
- encapsulation 
- information hiding
- order of magnitude

- Linear Structures
- abstract data types stack | queue | deque | list
- ADTs stack
- prefix | infix | postfix 
- Algorithmic Thinking 
- **Amortized Constant Space Complexity**
- Self Referential Object
- Contiguous Memory
- Non-Contiguous Memory
- Fixed Sized Partition
- Variable sized Partition
- internal fragmentation -> Memory wastage inside a partition
- Most Recently Used (MRU)
- Asymptotic Analysis 


-----------------------------------------------------------------------------------------------------

References
----------

- [Time Complexity Python](https://wiki.python.org/moin/TimeComplexity)

###### Gerry_Jenkins

* [What Is Computer Science?](https://runestone.academy/runestone/books/published/pythonds3/Introduction/WhatIsComputerScience.html)

**NOTE**

Worth to check is Gerry Jenkins Playlist in Youtube, where he covers Algorithm, Data Structures and Computer Science focused around Python ---> [HERE](https://www.youtube.com/c/GerryJenkins)

-----------------------------------------------------------------------------------------------------


Projects
--------


- [awesome-algorithms --GITHUB--](https://github.com/tayllan/awesome-algorithms)

- [TheAlgorithms --GITHUB--](https://github.com/TheAlgorithms/Python)

- [CookSheets-Algorithms --GITHUB--](https://github.com/simsekhalit/CookSheets-Algorithms)

- [algorithms --GITHUB--](https://github.com/keon/algorithms)

- [python-sortedcontainers --GITHUB--](https://github.com/grantjenks/python-sortedcontainers)

- [Algorithm-visualizer](https://algorithm-visualizer.org/)


-----------------------------------------------------------------------------------------------------

Notes
-----


### [Books and Learning](learn_resources.md)