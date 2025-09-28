---
tags:
  - algorithm
  - graphs
  - breadth-first-search
date: 2025-09-26
---
BFS Breadth-First-Search
=========

Content
---------------

* [BFS Breadth-First-Search (Python 🐍)](./Python/BFS%20Breadth-First-Search%20(Python%20🐍).md)

Documentation
-------------

- [Breadth-first search WIKI](https://en.wikipedia.org/wiki/Breadth-first_search)

**Breadth first search (BFS)** is one of the easiest algorithms for searching a graph. It also serves as a prototype for several other important graph algorithms that we will study later.

It uses the opposite strategy of [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search), which instead explores the node branch as far as possible before being forced to backtrack and expand other nodes.


Traversal means visiting all the nodes of a graph. Breadth First Traversal or Breadth First Search is a recursive algorithm for searching all the vertices of a graph or tree data structure.

1. Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.

2. If there are no remaining adjacent vertices left, remove the first vertex from the queue.

3. Repeat step 1 and step 2 until the queue is empty or the desired node is found.

#### Time Complexity
Since all of ​the nodes and vertices are visited, the time complexity for BFS on a graph is: 
`O(V+E);` 

- V = Number of Vertices. 
- E = Number of edges.

> Simple demo:

```python

GRAPH ={
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f'],
    'd': [],
    'e': ['f'],
    'f': []
}


def bfs(graph, source):
    visited = [source]
    queue = [source]
    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
    return [n.upper() for n in visited]


tree = bfs(GRAPH, 'a')
print(tree)
# ['A', 'B', 'C', 'D', 'E', 'F']


```

--------------------------------

#### Level Order Binary Tree Traversal

- [Breadth-first search / level order](https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search_/_level_order)

Trees can also be traversed in level-order, where we visit every node on a level before going to a lower level. This search is referred to as breadth-first search (BFS), as the search tree is broadened as much as possible on each depth before going to the next depth. 


###### Tree traversal | Tree search | Walking the tree | Graph traversal | Binary tree

- [Tree traversal WIKI](https://en.wikipedia.org/wiki/Tree_traversal)
- [Graph traversal WIKI](https://en.wikipedia.org/wiki/Graph_traversal)
- [Binary tree WIKI](https://en.wikipedia.org/wiki/Binary_tree)

    >  Depth-first search
    > Breadth-first search
    > [Iterative deepening depth-first search](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
    > [Monte Carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)


Guide & Areas of Study
-----------------------

- Copying [garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) 
- [Cheney's algorithm](https://en.wikipedia.org/wiki/Cheney%27s_algorithm)
- Finding the shortest path between two nodes u and v, with path length measured by number of edges (an advantage over depth-first search)
- [(Reverse) Cuthill–McKee mesh numbering](https://en.wikipedia.org/wiki/Cuthill%E2%80%93McKee_algorithm)
- [Ford–Fulkerson method](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm) for computing the [maximum flow](https://en.wikipedia.org/wiki/Maximum_flow_problem) in a [flow network](https://en.wikipedia.org/wiki/Flow_network)
- Serialization/Deserialization of a binary tree vs serialization in sorted order, allows the tree to be re-constructed in an efficient manner.
- Construction of the failure function of the [Aho-Corasick](https://en.wikipedia.org/wiki/Aho-Corasick) pattern matcher.
- Testing [bipartiteness of a graph](https://en.wikipedia.org/wiki/Bipartite_graph#Testing_bipartiteness)

PSEUDOCODE

```bash
procedure BFS(G, v) is
    create a queue Q
    enqueue v onto Q
    mark v
    while Q is not empty do
        w ← Q.dequeue()
        if w is what we are looking for then
            return w
        for all edges e in G.adjacentEdges(w) do
            x ← G.adjacentVertex(w, e)
            if x is not marked then
                mark x
                enqueue x onto Q
    return null

```

Terms & Keywords
----------------

* queue (First In First Out
* [Stack (abstract data type) WIKI](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) 
* [Branching factor](https://en.wikipedia.org/wiki/Branching_factor)
*  adjacency list | adjacency matrix
* [Implicit graph](https://en.wikipedia.org/wiki/Implicit_graph)
* BFS ordering

References
----------

- [Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [Level Order Binary Tree Traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/)
- [Component (graph theory)](https://en.wikipedia.org/wiki/Component_(graph_theory))
- [Routing (electronic design automation)](https://en.wikipedia.org/wiki/Routing_(electronic_design_automation))

Notes
-----

In a **Breadth First search** if you instead of a Queue you use a **Priority Queue** and define a sorting function on the nodes such that the node with the lowest cost is at the top of the Priority Queue you basically are doing a **Dijkstra (Heap method)**

 This allows us to find the best path through a graph in O(m * log(n)) time where n is the number of vertices and m is the number of edges in the graph.

 - [Source](https://www.topcoder.com/community/competitive-programming/tutorials/introduction-to-graphs-and-their-data-structures-section-3/)
