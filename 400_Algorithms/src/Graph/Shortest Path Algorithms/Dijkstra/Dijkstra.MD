---
tags:
  - algorithm
  - graphs
  - path-algorithms
  - dijkstra
date: 2025-09-26
---
Dijkstra
========


Dijkstra Algorithm finds shortest paths between nodes in a graph for a given source node in the graph, the results is based on the relative point of the source path., find Path between 2 vertices | nodes in a Graph with minimum Edges's weights sum cost.

Content
---------------

* [Dijkstra (Python 🐍)](./Python/Dijkstra%20(Python%20🐍).md)

Documentation
-------------

Dijkstra Algorithm is based on the principle of **Relaxation** an approximation to the correct distance is gradually replaced by more accurate values till the shortes distance path is found. 

It uses a **priotity queue** to greedily select the closest vertex that hasn't been processed, then performs the relaxation process on all of its neighbors. 


It uses a **priotity queue** to greedily select the closest vertex that hasn't been processed, then performs the relaxation process on all of its neighbors. 

Is a graph search Algorithm that solves the **Single-source [shortes path problem](https://en.wikipedia.org/w/index.php?title=Shortest_path_problem)** for a [Graph](https://en.wikipedia.org/wiki/Graph#Mathematics) with **non-negative edge path** costs, producing a **[Shortest-path tree](https://en.wikipedia.org/wiki/Shortest-path_tree)**

This Algorithm is often used in [routing](https://en.wikipedia.org/w/index.php?title=Routing) and as a [subroutine](https://en.wikipedia.org/w/index.php?title=Subroutine) in other graph algorithms. 


===================================== < Initial Configs > ==================================  

1. Assign to every node a tentative **distance value**: set it to zero for **Initial Node** &  **to infinity for all other nodes,** calculate in a **Graph** N of Vertices (Nodes) and Edges (Paths). 

2. Mark all nodes **unvisited** & inserte into a **Unvisited Sets**.  

===================================== < Loops > ==================================  

3. Set the initial node as **current**.  Calculate their tentative distances of the unvisited neighbors. 

4. When done considering all of the neighbors of the **current** node, mark the current node as **visited And remove it from unvisited set.** 

5. Check if another need to keep looping. I

        IF planning a route between two specific nodes

if the destination node has been marked visited then stop. Thealgorithm has finished. 

        IF planning a complete traversal;occurs when there is no connection between the initial node and remaining unvisited nodes

if the smallest tentative distance among the nodes in the unvisited set is infinity then stop. The algorithm has finished. 

If none of the above statements are true proceed to step 6.

6. Select the unvisited node that is marked with the smallest tentative distance, and set it as the new **current node**  Loop starts again to step 3.

===================================== < End of Loop > ================================== 


### Pseudocode

```
Q = The set of all nodes in Graph which haven't been visited

V = Vertex 

u := Vertex in Q with smallest distance in dist

dist = All Nodes in Graph with Distances / weight of Path. Initially set to Infinity then a distance when is found

prev = All Nodes in Graph set initially to undefined, keep tracks of the best/shortes Path

source = Initial Node

dist_between(u, v) = Function that calcs distance between current node and neighbour node

function Dijkstra(Graph, source):

    for each vertex V in Graph:  // Create the Graph and set Distance / Path
        dist[v] := INFINITY;      All V are set to INFINITY's distance 
        prev[v] := UNDEFINED;
    end for

    dist[source] := 0;           // Set initial node to distance 0 |is always 0
    Q := Set of all Unvisited nodes in Graph;

    while Q is not empty:
        u := Vertex in Q with smalles distance in dist[];
        remove u from Q;
        u = Visited True;

        if dist[u] = INFINITY;
            break;
        end if

        neighbours := neighbour v of u;
        for each neighbour N in neighbours:
            neighbour_distance := dist[u] + dist_between(u, v);

            if neighbour_distance < dist[v]:
                dist[v] := neighbour_distance;
                prev[v] := u;
                remove-key v in q;
            end if
        end for
    end while
    return dist;
end function

```


### Running time 

#### Original Implementation

The Original Implementation doesn't use a **[Min-Priority-Queue](https://en.wikipedia.org/wiki/Priority_queue)** runs in  O(V**2), V == where is the number of vertices.


#### More efficiency

For [sparse graphs](https://en.wikipedia.org/wiki/Dense_graph), that is, graphs with far fewer than O(V**2) edges, storing  the  graph  in  the  form  of  [adjacency  lists](https://en.wikipedia.org/w/index.php?title=Adjacency_list)  and  using  a  [self-balancing  binary  search  tree](https://en.wikipedia.org/w/index.php?title=Self-balancing_binary_search_tree),  [binaryheap](https://en.wikipedia.org/w/index.php?title=Binary_heap),  [pairing  heap](https://en.wikipedia.org/w/index.php?title=Pairing_heap),  or  [Fibonacci  heap](https://en.wikipedia.org/w/index.php?title=Fibonacci_heap)  as  a  [priority  queue](https://en.wikipedia.org/w/index.php?title=Priority_queue)  to  implement  extracting  minimum  efficiently.  

With a self-balancing  binary  search  tree  or  binary  heap,  the  algorithm  requires  time 


-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------


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

### Mathematics | Physics | Programming  

- [Logarithm](https://en.wikipedia.org/wiki/Logarithm)
- [Wavefront](https://en.wikipedia.org/w/index.php?title=Wavefront)
- [Dense graph](https://en.wikipedia.org/wiki/Dense_graph)
- [Vertex (graph theory)](https://en.wikipedia.org/w/index.php?title=Vertex_%28graph_theory%29)

- [Linear programming](https://en.wikipedia.org/w/index.php?title=Linear_programming)
- [l linear program for computing shortest  paths](https://en.wikipedia.org/wiki/Shortest_path_problem#Linear_programming_formulation)
- [Dual linear program](https://en.wikipedia.org/w/index.php?title=Dual_linear_program)
- [Dynamic programming](https://en.wikipedia.org/w/index.php?title=Dynamic_programming)

### Real world implementations

- [Routing protocol](https://en.wikipedia.org/w/index.php?title=Routing_protocol)
- [Link-state routing protocol](https://en.wikipedia.org/w/index.php?title=Link-state_routing_protocol)
- [Open Shortest Path First](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)
- [IS-IS](https://en.wikipedia.org/w/index.php?title=IS-IS)
- [Motion planning](https://en.wikipedia.org/w/index.php?title=Motion_planning)


-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------


- Graph = Map = G ; 
- Vertex = Intersections = V 
- Vertex = u
- Edge = Roads | Path = E
- Edge's Length = Weight = W
- Path = P = ( v 1 , v 2 , … , v n ) ∈ V × V × ⋯ × V 
- Spanning Tree = T 
- Source = Root Node = Initial Node

- Current Node
- Unvisited Node
- Unvisited Set
- Node's neighbors 
- Tentative Distance Current Node To neighbors 


-----------------------------------------------------------------------------------------------------

References
----------

### Resources

- [algorithm.pdf](http://www.cse.unt.edu/~tarau/teaching/AnAlgo/Dijkstra's%20algorithm.pdf)
- [Single-Source Shortest Paths – Dijkstra’s Algorithm](https://www.techiedelight.com/single-source-shortest-paths-dijkstras-algorithm/)
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Shortest-path tree](https://en.wikipedia.org/wiki/Shortest-path_tree)
- [Shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem)
- [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree)

-----------------------------------------------------------------------------------------------------

Notes
-----



