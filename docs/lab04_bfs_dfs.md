# Lab 4: Graph Traversal - BFS and DFS Algorithms

## 📌 Lab Overview

This lab explores fundamental graph traversal algorithms essential for artificial intelligence and computer science. Students implement **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to navigate graph structures systematically.

## 🎯 Learning Objectives

- Understand graph representation using adjacency lists
- Implement iterative Breadth-First Search with queues
- Implement recursive Depth-First Search
- Manage visited nodes to prevent infinite loops
- Compare traversal order differences between BFS and DFS

## 📚 Libraries Used

```python
from collections import deque
```

---

## 📝 Tasks

### Task 1: Breadth-First Search (BFS)

**Objective:** Implement BFS to traverse a graph level by level using a queue.

#### Algorithm Overview

BFS explores nodes in layers, visiting all neighbors at the current depth before moving deeper.

**Time Complexity:** O(V + E) where V = vertices, E = edges  
**Space Complexity:** O(V) for the queue and visited set

#### Implementation

```python
def bfs(graph, start):
    visited = set()               # keep track of visited nodes
    queue = deque([start])        # queue for BFS

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()    # remove element from queue

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # add neighbors that are not visited
            queue.extend(graph[node] - visited)

    print()   # new line after traversal
```

#### How It Works

1. **Initialize:** Create empty visited set and queue with start node
2. **Loop:** While queue is not empty
3. **Dequeue:** Remove front node from queue
4. **Check:** If not visited, mark as visited and print
5. **Enqueue:** Add all unvisited neighbors to queue
6. **Repeat:** Until queue is empty

**Visualization:**
```
Graph:     A
          / \
         B   C
        /|   |\
       D E   F G
         |
         H

BFS from A: A B C D E F G H
```

---

### Task 2: Depth-First Search (DFS)

**Objective:** Implement DFS to traverse a graph by going as deep as possible before backtracking.

#### Algorithm Overview

DFS explores as far as possible along each branch before backtracking, using recursion or a stack.

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V) for recursion stack and visited set

#### Implementation

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        # recursively visit neighbors
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

#### How It Works

1. **Base Case:** If visited is None, create new set
2. **Check:** If current node not visited
3. **Visit:** Print node and mark as visited
4. **Recurse:** Call DFS on each unvisited neighbor
5. **Backtrack:** Return when all neighbors explored

**Visualization:**
```
Graph:     A
          / \
         B   C
        /|   |\
       D E   F G
         |
         H

DFS from A: A B D E H C F G
```

---

## 🔍 Graph Representation

Both algorithms use an **adjacency list** represented as a dictionary of sets:

```python
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E'}
}
```

**Why sets?**
- O(1) membership checking
- Automatic duplicate prevention
- Order doesn't matter for neighbors

---

## ⚖️ BFS vs DFS Comparison

| Feature | BFS | DFS |
|---------|-----|-----|
| **Data Structure** | Queue (FIFO) | Stack/Recursion (LIFO) |
| **Traversal Order** | Level by level | Deep then backtrack |
| **Path Finding** | Shortest path | Any path |
| **Memory** | More memory (wide graphs) | Less memory (deep graphs) |
| **Implementation** | Iterative with deque | Recursive or stack |
| **Use Cases** | Shortest path, web crawlers | Maze solving, topological sort |

---

## 💡 Key Concepts

### Visited Set Management
```python
visited = set()  # O(1) lookup time
```
**Why?** Prevents infinite loops in cyclic graphs.

### Queue vs Stack
- **BFS uses Queue:** First In, First Out (FIFO)
- **DFS uses Stack:** Last In, First Out (LIFO, via recursion)

### Graph Properties
- **Connected:** All nodes reachable from start
- **Undirected:** Edges work both ways (A→B and B→A)
- **Cyclic:** Contains loops

---

## 🎓 Skills Acquired

✅ Graph representation using adjacency lists  
✅ BFS implementation with queues  
✅ DFS implementation with recursion  
✅ Visited set management for cycle detection  
✅ Understanding traversal order differences  
✅ Time and space complexity analysis  

## 🌍 Real-World Applications

### BFS Applications
- **Social Networks:** Find degrees of separation
- **GPS Navigation:** Shortest route finding
- **Web Crawlers:** Level-by-level page discovery
- **Network Broadcasting:** Message propagation

### DFS Applications
- **Maze Solving:** Finding any exit path
- **Dependency Resolution:** Package managers
- **Cycle Detection:** Deadlock detection
- **Topological Sorting:** Task scheduling

---

## 🔗 Related Files

- **Source Code:** [lab04_bfs_dfs.py](../lab04_bfs_dfs.py)
- **Previous Lab:** [Lab 3: NumPy and Pandas](lab03_numpy_pandas.md)
- **Next Lab:** [Lab 5: AI Search Algorithms](lab05_astar_hillclimbing.md)

---

*Author: Mussa Khan | BS-AI (4th Year)*
