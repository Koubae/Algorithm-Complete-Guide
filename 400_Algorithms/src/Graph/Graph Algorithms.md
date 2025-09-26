---
tags:
  - algorithm
  - data-structure
  - graphs
  - directed-graph
  - weighted-graph
  - undirected-graph
  - unweighted-graph
  - graph-algorithm
  - dijkstra
date: 2025-09-26
---

Graph-Algorithms
=========

*Graph Traversals (BFS, DFS)*

Content
---------------


* [Graph-Traversal](./Graph-Traversal/Graph%20Traversal.md)
  * BFS
  * DFS
* [Shortest Path Algorithms](./Shortest%20Path%20Algorithms/Shortest%20Path%20Algorithms.md)
  * Dijkstra’s Algorithm
  * Bellman–Ford Algorithm
  * Floyd–Warshall Algorithm
  * A* Search
* [Minimum Spanning Tree Algorithms](./Minimum%20Spanning%20Tree%20Algorithms/Minimum%20Spanning%20Tree%20Algorithms.md)
  * Prim’s Algorithm
  * Kruskal’s Algorithm 
* Other Graph Problems
  * Topological Sort (DAGs) 
  * Connectivity (Union-Find / DSU)
  * Cycle Detection


Documentation | Guide & Areas of Study
-----------------------


The following two are the most commonly used representations of a graph:

1. Adjacency Matrix
2. Adjacency List

3. Incidence Matrix 
4. Incidence List

#### Adjacency Matrix

* [Adjacency Matrix](https://github.com/Koubae/Algorithm-Complete-Guide/blob/master/Graph-Algorithms/graph_adjacency_matrix.py)
- [Adjacency matrix WIKI](https://en.wikipedia.org/wiki/Adjacency_matrix)

Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. 
 Adjacency matrix for undirected graph is **always symmetric.**

- Graph node represented with adj
- Edge = adj[i][j] = 1 | Edge / Path from i to j.
- Weigthted Graph = adj[i][j] = w (n)

``` bash
Graph = [
    [0, 1, 0, 0, 1]  # Node 1
    [1, 0, 1, 1, 1]  # Node 2
    [0, 1, 0, 1, 0]  # Node 3
    [0, 1, 1, 0, 1]  # Node 4
    [1, 1, 0, 1, 0]  # Node 5

     1  2  3  4  5
]
```


- #### Adjacency List

- [Adjacency list WIKI](https://en.wikipedia.org/wiki/Adjacency_list)

adjacency list is a collection of unordered lists used to represent a finite graph. 


### Spanning Tree & Minimum Spanning Tree

*  Undirected graph

The edges do not point in any direction (ie. the edges are bidirectional), hence if there is a path between V a and V b you can go (a, b) or reverse (b, a).

* Connected graph

Paths are one direction, V a and V b, if only path (a, b) is set then you can't go (b, a).

* **Spanning tree**

A spanning tree is a sub-graph of an *undirected or connected graph*, which includes all the vertices of the graph with a **minimum** possible number of edges. 

If a vertex is missed, then it is not a spanning tree.

The edges may or may not have weights assigned to them.

The total number of spanning trees with n vertices that can be created from a complete graph is equal to n(n-2).

If we have n = 4, the maximum number of possible spanning trees is equal to 44-2 = 16. Thus, 16 spanning trees can be formed from a complete graph with 4 vertices.

* **Minimum Spanning Tree**

A minimum spanning tree is a spanning tree in which the sum of the weight of the edges is as minimum as possible.


- Prim's Algorithm
- Kruskal's Algorithm
- Dijkstra's Algorithm


Terms & Keywords
----------------

- [Graph theory](https://en.wikipedia.org/wiki/Graph_theory#Applications)
- [Bipartite graph](https://en.wikipedia.org/wiki/Bipartite_graph)

- Set or ordered Pair (u, v) != (v, u)
- directed graph | **di-graph**
- weight | value | cost | Distance 
- Sparse Graph (containing less n of Edges)
- Undirected Graph [WIKI](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#undirected)
- Directed graphs


Algorithms
-------------


### alpha–beta pruning

* [alpha–beta pruning](https://en.wikipedia.org/w/index.php?title=Alpha%E2%80%93beta_pruning)


### A* algorithm

* [A* algorithm](https://en.wikipedia.org/w/index.php?title=A%2A_search_algorithm)

The A* algorithm is a generalization of Dijkstra's algorithm that cuts down on the size of the subgraph that must be explored,


### B*

* [B*](https://en.wikipedia.org/w/index.php?title=B%2A)

### Backtracking

* [Backtracking](https://en.wikipedia.org/w/index.php?title=Backtracking)


### Beam search

* [Beam search](https://en.wikipedia.org/w/index.php?title=Beam_search)


### Bellman–Ford algorithm

Unlike Dijkstra's algorithm, the Bellman–Ford algorithm can be used on graphs with negative edge weights, as long as the graph contains no [negative cycle](https://en.wikipedia.org/wiki/Negative_cycle) reachable from the source vertex s.


### Best-first search

* [Best-first search](https://en.wikipedia.org/w/index.php?title=Best-first_search)


### Bidirectional search

* [Bidirectional search](https://en.wikipedia.org/w/index.php?title=Bidirectional_search)


### Borůvka's algorithm

* [Borůvka's algorithm](https://en.wikipedia.org/w/index.php?title=Bor%C5%AFvka%27s_algorithm)


### Branch and bound

* [Branch and bound](https://en.wikipedia.org/w/index.php?title=Branch_and_bound)


### Breadth-first search

- [Breadth First Search (BFS) | Iterative & Recursive Implementation](https://www.techiedelight.com/breadth-first-search/)


### British Museum algorithm

* [British Museum algorithm](https://en.wikipedia.org/w/index.php?title=British_Museum_algorithm)

### D*

* [D*](https://en.wikipedia.org/w/index.php?title=D%2A)*

### Depth-first search

*  [Depth-first search](https://en.wikipedia.org/w/index.php?title=Depth-first_search)

### Iterative deepening depth-first search

* [Iterative deepening depth-first search](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)

### Dijkstra

* [Dijkstra](https://github.com/Koubae/Algorithm-Complete-Guide/tree/master/Graph-Algorithms/Dijkstra)

### Edmonds' algorithm

* [Edmonds' algorithm](https://en.wikipedia.org/w/index.php?title=Edmonds%27_algorithm)

### FloydWarshall algorithm14Floyd–Warshall algorithm

* [FloydWarshall algorithm14Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)


### Fringe search

* [Fringe search](https://en.wikipedia.org/w/index.php?title=Fringe_search)

### Hill climbing

*  [Hill climbing](https://en.wikipedia.org/w/index.php?title=Hill_climbing)

### Iterative deepening A*

* [Iterative deepening A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)

### Iterative deepening depth-first search

* [Iterative deepening depth-first search](https://en.wikipedia.org/w/index.php?title=Iterative_deepening_depth-first_search)

### Kruskal's algorithm

* [Kruskal's algorithm](https://en.wikipedia.org/w/index.php?title=Kruskal%27s_algorithm)


### Johnson's algorithm.

- [Source](https://en.wikipedia.org/wiki/Johnson%27s_algorithm)


### Prim's algorithm

- [Source](https://en.wikipedia.org/wiki/Prim%27s_algorithm)


### Fast marching method 

- [Source](https://en.wikipedia.org/wiki/Fast_marching_method)


### Other

#### **Heap queue algorithm / priority queue algorithm**

- **heapq — Heap queue algorithm** [--Python Docs--](https://docs.python.org/3/library/heapq.html)
- [--Python Docs-- nsmallest](https://docs.python.org/3/library/heapq.html#heapq.nsmallest)


- **Selection algorithm** [WIKI](https://en.wikipedia.org/wiki/Selection_algorithm)

- **Cache replacement policies**[WIKI](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))

- **Round-robin scheduling**[WIKI](https://en.wikipedia.org/wiki/Round-robin_scheduling)

- **Tail Recursion** [StackOverflow](https://stackoverflow.com/questions/33923/what-is-tail-recursion)

- [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)


#### Tree traversal | Tree search | Walking the tree | Graph traversal | Binary tree

- [Tree traversal WIKI](https://en.wikipedia.org/wiki/Tree_traversal)
- [Graph traversal WIKI](https://en.wikipedia.org/wiki/Graph_traversal)
- [Binary tree WIKI](https://en.wikipedia.org/wiki/Binary_tree)

* Depth-first search
* Breadth-first search
  * [Iterative deepening depth-first search](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
  * [Monte Carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)


References
----------


### Related Algorithms

- [Bellman–Ford algorithm](http://www.cse.unt.edu/~tarau/teaching/AnAlgo/Dijkstra%27s%20algorithm.pdf#%5B%7B%22num%22%3A31%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C297.9829%2C787.6635%2C0%5D)
- [A* search](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Prim's algorithm](https://en.wikipedia.org/w/index.php?title=Prim%27s_algorithm)
- [Breadth-first search](https://en.wikipedia.org/w/index.php?title=Breadth-first_search)
- [Asymptotic computational complexity](https://en.wikipedia.org/w/index.php?title=Asymptotic_computational_complexity)

### Algorithm related

- [Priority queue](https://en.wikipedia.org/wiki/Priority_queue)
- [no negative cycle](https://en.wikipedia.org/wiki/Shortest_path_problem#Related_problems)
- [Consistent heuristic](https://en.wikipedia.org/w/index.php?title=Consistent_heuristic)
- [Admissible heuristic](https://en.wikipedia.org/w/index.php?title=Admissible_heuristic)
- [Minimum spanning tree](https://en.wikipedia.org/w/index.php?title=Minimum_spanning_tree)
- [Fibonacci heap](https://en.wikipedia.org/wiki/Fibonacci_heap)

- [Brodal queue](https://en.wikipedia.org/wiki/Brodal_queue)
- [Motion planning](https://en.wikipedia.org/wiki/Motion_planning)
- [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree)
- [Minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree)
- [Binary tree](https://en.wikipedia.org/wiki/Binary_tree)

### Mathematics | Physics | Programming  

- [Logarithm](https://en.wikipedia.org/wiki/Logarithm)
- [Wavefront](https://en.wikipedia.org/w/index.php?title=Wavefront)
- [Dense graph](https://en.wikipedia.org/wiki/Dense_graph)
- [Vertex (graph theory)](https://en.wikipedia.org/w/index.php?title=Vertex_%28graph_theory%29)

- [Linear programming](https://en.wikipedia.org/w/index.php?title=Linear_programming)
- [l linear program for computing shortest  paths](https://en.wikipedia.org/wiki/Shortest_path_problem#Linear_programming_formulation)
- [Dual linear program](https://en.wikipedia.org/w/index.php?title=Dual_linear_program)
- [Dynamic programming](https://en.wikipedia.org/w/index.php?title=Dynamic_programming)
- [Graph theory](https://en.wikipedia.org/wiki/Graph_theory)
- [Graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph)

### Real world implementations

- [Routing protocol](https://en.wikipedia.org/w/index.php?title=Routing_protocol)
- [Link-state routing protocol](https://en.wikipedia.org/w/index.php?title=Link-state_routing_protocol)
- [Open Shortest Path First](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)
- [IS-IS](https://en.wikipedia.org/w/index.php?title=IS-IS)
- [Motion planning](https://en.wikipedia.org/w/index.php?title=Motion_planning)

