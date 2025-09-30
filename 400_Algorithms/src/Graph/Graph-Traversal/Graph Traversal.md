---
tags:
  - algorithm
  - graphs
  - graph-traversal
  - breadth-first-search
  - depth-first-search
date: 2025-09-26
---
Graph Traversal
=========

Content
---------------

* [BFS Breadth-First-Search](./BFS%20Breadth-First-Search/BFS%20Breadth-First-Search.MD)
* [DFS Depth-First-Search](./DFS%20Depth-First-Search/DFS%20Depth-First-Search.MD)

Related
----------------------------

Imagine cities connected by roads:

- A connects to B (2), C (5), D (1)    
- B connects to E (3)    
- D connects to C (2), E (6)    
- C connects to F (7)    
- F connects to E (4)

```bash
     (2)
 A --------> B
 |  \        |
 |   \       v
(5)  (1)    (3)
 |     \     |
 v      v    v
 C <---- D -> E
  \            ^
   \----(7)----/
         F
```

```python
graph = {
    "A": [("B", 2), ("C", 5), ("D", 1)],
    "B": [("E", 3)],
    "C": [("F", 7)],
    "D": [("C", 2), ("E", 6)],
    "E": [],
    "F": [("E", 4)]
}
```
