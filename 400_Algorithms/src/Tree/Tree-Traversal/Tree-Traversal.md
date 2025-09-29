---
tags:
  - algorithm
  - trees
  - traversal-algorithm
  - inorder
  - preorder
  - postorder
  - level-order
date: 1991-05-11
---

Tree-Traversal
=========

*Inorder, Preorder, Postorder, Level Order*

Content
---------------

* [Inorder](./Inorder/Inorder.MD)

* [Tree-Traversal Go](./go/Tree-Traversal%20(Go%20🦫).md)
* [Tree Traversal in Python 🐍](./Python/Tree-Traversal%20(Python%20🐍).md)


Related
----------------------------

### What does preorder | inorder | postorder means?


- Preorder, Inorder, Postorder = **flavors of DFS**
- Level-order = **BFS**

##### 🌲 DFS (Depth-First Search)

- General **strategy**: explore as far down a branch as possible before backtracking.    
- In trees, DFS can be expressed in **three main orders**:    
    - **Preorder** → Visit root → left → right        
    - **Inorder** → Visit left → root → right        
    - **Postorder** → Visit left → right → root        
- So **preorder is one type of DFS** (but not the only one).
    
---

##### 🌳 BFS (Breadth-First Search)

- General **strategy**: explore neighbors level by level before going deeper.    
- In trees, BFS is exactly what we usually call **Level-Order traversal**.




