Type of Data-Structures
==================

_Data Structures is a data storage format. It's the collection of values and the format they are stored in, 
the relationships between the values in the collections as well as the operations applied on the data stored in 
the structure._

A data structure is a model where data is organized, managed and stored in a format that enables efficient access and modification of data. There are various types of data structures commonly available. It is up to the programmer to choose which data structure to use depending on the data.

The choice of a particular one can be considered based on the following points:

1) It must be able to process the data efficiently when necessary.
2) It must be able to represent the inherent relationship of the data in the real world.

* Array
* Linked Lists
* Doubly Linked lists
* Maps / Dictionaries
* Trees
* Stacks & Queues 
* Heaps 
* Graphs 
* Runtime Analysis 
* Searching & Sorting 
* Recursion & DP (Dynamic Programming)

* Linear Data structure
  * Array
  * Stack 
  * Queues
  * Linked List

* Non-Linear Data structure
  * Graph
  * Trees
    * Binary Tree
    * Binary Search Tree
    * AVL Tree
    * B-Tree
    * B+ Tree
    * Red-Black Tree

#### Data Structure Classification

* Linear Data Structures
  * Arrays
  * Linked Lists 
  * Stacks 
  * Queues
* Non-Linear Data Structures
  * Trees 
  * Heaps
  * Graphs
  * Hash Tables / Maps / Dictionaries


Linear Data Structures
----------------------

_A linear data structure’s elements form a sequence. Every element in the structure has some element before and after it._

* [educative.io | Contiguous memory](https://www.educative.io/answers/contiguous-memory)
* [Difference between Contiguous and Noncontiguous Memory Allocation](https://www.geeksforgeeks.org/difference-between-contiguous-and-noncontiguous-memory-allocation/)

### Arrays 

_An array holds a fixed number of similar elements that are stored under one name. These elements are stored in contagious memory locations . The elements of an array can be accessed using one identifier._

Grow pattern of Python's `list` is for memory allocations:
**0, 4, 8, 16, 25, 35, 46**

This is called **Amortized Constant Space Complexity**

* homogeneous : Containing the same value types
* heterogeneous : Containing mixed type of values 

* linear arrays

#### Column Major Representation

_In this form, the elements are stored column by column. m elements of the first column are stored in the first m locations, elements of the second column element are stored in the next m locations, and so on._

#### Row Major Formula

_In this form, the elements are stored row by row. n elements of the first row are stored in the first n locations, elements of the second row elements are stored in the next n locations, and so on._


### Linked List

_**A linked list is a linear data structure where each element is a separate object, known as a node . Each node contains some data and points to the next node in the structure, forming a sequence .**_

Pointer to start (index 0 ) and no pointer to the end (index -1 )

A linked list is a **Self Referential Object**


#### Types of Linked Lists

_A linked list is designed depending on its use. The 3 most common types of a linked list are:_

- Singly Linked List
- Doubly Linked List
- Circular Linked List


### Stacks 

_Stacks are a type of linear data structures that store data in an order known as the Last In First Out (LIFO)  order. This property is helpful in certain programming cases where the data needs to be ordered._

Stacks can be visualised like a stack of plates on a table. Only the top plate is accessible by the user at any given instant. The other plates are hidden and are not accessible by the user. The last plate that is kept on the stack is retrieved first.

#### Operations

* Push : This is used to add (or push) an element to the stack. The element always gets added to the top of the current stack items.
* Pop : This is used to remove (or pop) an element from the stack. The element always gets popped off from the top of the stack.
* Peek : The peek operation is used to return the first element of the stack without removing the element. It is a variation of the pop operation.

#### About the top pointer
To efficiently add or remove data, a special pointer is used which keeps track of the last element inserted in the structure. 
This pointer updates continuously and keeps a check on the overflow and underflow conditions.


### Queues 

_Queues are a type of linear data structures that store data in an order known as the First In First Out (FIFO)  order. This property is helpful in certain programming cases where the data needs to be ordered._

#### Operations

* Enqueue Operation : The Enqueue is used to add an element to the queue. The element always gets added to the end of the current queue items.
* Dequeue Operation: The Dequeue is used to remove an element from the queue. The element always gets removed from the front of the queue. 


#### The front and rear pointer

To efficiently add or remove data from the queue, two special pointers are used which keep track of the first and last element in the queue. These pointers update continuously and keep a check on the overflow and underflow conditions.

The front pointer always points to the position where an element would be dequeued next. The rear pointer always points to the position where an element would be enqueued next.


#### Variations of a queue

* **Double-Ended queue (Deque)**

In a standard queue, insertion can only be done from the back and deletion only from the front. 
A double-ended queue allows for insertion and deletion from both ends.

* **Circular Queue (Circular Buffer)**

A circular queue uses a single, fixed-size buffer as if it were connected end-to-end like a circle.

This is an efficient implementation for a queue that has fixed maximum size.
There is no shifting involved and the whole queue can be used for storing all the elements.

* *+Priority Queue**

A priority queue assigns a priority to each element in the queue. 
This priority determines which elements are to be deleted and processed first. 
There can be different criteria’s for the priority queue to assign priorities.

An element with the highest priority gets processed first. 
If there exist two elements with the same priority, then the order 
of which the element was inserted is considered.



Non-Linear Data Structures
----------------------

_A non-linear data structure’s elements do not form a sequence. Every element may not have a unique element before and after it._

### Trees

_A tree is a data structure that simulates a hierarchical tree, with a root value and the children as the subtrees, represented by a set of linked nodes._

#### Basic Terminology

* **Root:** The first node in a tree is called as Root Node. Every tree must have one Root Node.
* **Parent Node**  The node which is a predecessor of any node is called a Parent Node, that is, the node which has a branch from it to any other node is called as the Parent node.
* **Child Node** The node which is descendant of any node is called as Child Node. Any parent node can have any number of child nodes. All the nodes except root are child nodes.
* **Siblings** Nodes which belong to the same Parent are called as Siblings.
* **Leaf Node* In a tree data structure, the node which does not have a child is called a Leaf Node. They are also known as External Nodes or Terminal Nodes.
* **Internal Nodes** The node which has at least one child is called an Internal Node.
* **External Nodes** The node which has no child is called an External Node.
* **Degree**  The total number of children of a node is called a Degree of that Node. The highest degree of a node among all the nodes in a tree is called the Degree of the tree.
* **Level** In a tree, each step from top to bottom is called a Level.
* **Height** The total number of edges from the leaf node to a particular node in the longest path is called as Height of that Node.
* **Depth**  The total number of edges from the root node to a particular node is called the Depth of that Node.
* **Path**  The sequence of Nodes and Edges from one node to another node is called a Path.

#### Types of a tree

There are multiple types of trees with their various properties:

- General trees
- Tree Traversals
- Binary trees
  - Strictly Binary Tree
  - Complete Binary Tree
  - Extended Binary Tree
  - Threaded Binary Tree
  - Single-Threaded Binary Tree
  - Double-Threaded Binary Tree

- Binary Search trees
- M-way trees (Multiway trees)
  - B-Trees (a specialized M-way)
  - B+ Trees 
- AVL trees (self-balancing binary search tree)

### Heaps

* [Heap (data structure)](https://en.wikipedia.org/wiki/Heap_(data_structure))

_A heap is a specialized tree-based data structure that satisfies the heap property._
A heap is a complete binary tree that satisfies the  heap property. There are two types of heaps, the max heap and the min heap.

#### The heap property
The heap property says that is the value of Parent is either **greater than or equal** to (in a **max heap** ) 
or **less than or equal to** (in a **min heap**) the value of the Child.

A heap is described in memory using **linear arrays** in a sequential manner.

### Graphs 

_A graph data structure is used to represent relations between pairs of objects. It consists of nodes (known as vertices) that are connected through links (known as edges). The relationship between the nodes can be used to model the relation between the objects in the graph._

It consists of **nodes** (known as vertices) that are connected through **links** (known as edges). 
The relationship between the nodes can be used to model the relation between the objects in the graph. 
This is what makes graphs important in the real world.


#### Type of Graphs 

* Directed Graph
* Undirected Graphs


#### Basic Terminology in a graph

- **Vertex**: An individual data element of a graph is called Vertex.

- **Edge**: An edge is a connecting link between two vertices. An Edge is also known as Arc.

- **Mixed Graph**: A graph with undirected and directed edges is said to be a mixed graph.

- **Origin**: If an edge is directed, its first endpoint is said to be the origin of it.

- **Destination**: If an edge is directed, its first endpoint is said to be the origin of it and the other endpoint is said to be the destination of the edge.

- **Adjacency**: Two node or vertices are adjacent if they are connected through an edge.

- **Path**: The Path represents a sequence of edges between the two vertices.

- **Degree:** The total number of edges connected to a vertex is said to be the degree of that vertex.

- **In-Degree:** In-degree of a vertex is the number of edges which are coming into the vertex.

- **Out-Degree:** Out-degree of a vertex is the number of edges which are going out from the vertex.

- **Minimum Spanning Tree (MST):** A minimum spanning tree (MST) is a subset of the edges of a connected, edge-weighted (un)directed graph that connects all the vertices, without any cycles and with the minimum possible total edge weight.

- **Simple Graph:** A graph is said to be simple if there are no parallel and self-loop edges.

- **Directed acyclic graph (DAG):** A directed acyclic graph (DAG) is a graph that is directed and without cycles connecting the other edges. This means that it is impossible to traverse the entire graph starting at one edge.

- **Weighted Graph:** A weighted graph is a graph in which a number (known as the weight) is assigned to each edge. Such weights might represent for example costs, lengths or capacities, depending on the problem.

- **Complete Graph:** A complete graph is a graph in which each pair of vertices is joined by an edge. A complete graph contains all possible edges.

- **Connected graph:** A connected graph is an undirected graph in which every unordered pair of vertices in the graph is connected. Otherwise, it is called a disconnected graph.


#### Representation of a graph

* Adjacency List Representation
* Adjacency Matrix Representation

### Hash Tables / Maps / Dictionaries

_A Hash Table is a data structure where data is stored in an associative manner. The data is mapped to array positions by a hash function that generates a unique value from each key. The value stored in a hash table can then be searched in O(1) time using the same hash function which generates an address from the key._


