# Lab 4: Graph Traversal - BFS and DFS Algorithms
# Author: Mussa Khan
# Department: BS-AI (4th Semester)
# Subject: Artificial Intelligence
# Instructor: Farhan Zafar Kayani

# ================================================
# LAB TASKS: BFS and DFS Implementations
# ================================================

from collections import deque

# ------------------------------------------------
# Task 1: Breadth First Search (BFS)
# ------------------------------------------------

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


# ------------------------------------------------
# Task 2: Depth First Search (DFS)
# ------------------------------------------------

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        # recursively visit neighbors
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# ------------------------------------------------
# Graph Representation Used for Both Tasks
# ------------------------------------------------

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

# ------------------------------------------------
# Run Tasks
# ------------------------------------------------

print("\n--- Task 1: BFS Output ---")
bfs(graph, 'A')

print("\n--- Task 2: DFS Output ---")
dfs(graph, 'A')
print()   # new line after DFS


# ------------------------------------------------------
# Conclusion
# ------------------------------------------------------
# In this lab I learned how BFS and DFS work by implementing
# them step by step. I understood how BFS uses a queue to
# explore nodes level by level, while DFS uses recursion to
# go as deep as possible. This helped me understand graph
# traversal logic and how visited sets prevent infinite loops.
