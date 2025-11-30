# Lab 5: AI Search Algorithms - A* and Hill Climbing

## 📌 Lab Overview

This lab implements advanced AI search algorithms used for pathfinding and optimization. Students learn **A\* (A-star)** for informed pathfinding with heuristics and **Hill Climbing** for local optimization through iterative improvement.

## 🎯 Learning Objectives

- Implement A\* algorithm with heuristic evaluation
- Understand priority queues and f-score calculation
- Apply hill climbing for optimization problems
- Compare informed vs uninformed search strategies
- Analyze local optima and global optimization challenges

## 📚 Libraries Used

```python
import heapq
import random
```

---

## 📝 Tasks

### Task 1: A\* (A-star) Pathfinding Algorithm

**Objective:** Implement A\* to find optimal paths using both actual cost and heuristic estimates.

#### Algorithm Overview

A\* combines the benefits of Dijkstra's algorithm (guaranteed shortest path) with greedy best-first search (heuristic guidance) using the evaluation function:

**f(n) = g(n) + h(n)**

- **g(n):** Actual cost from start to node n
- **h(n):** Heuristic estimate from n to goal
- **f(n):** Total estimated cost through n

**Time Complexity:** O(E log V) with good heuristic  
**Space Complexity:** O(V)

#### Implementation

```python
import heapq

def a_star(graph, start, goal, heuristic):
    # g score: cost from start to current node
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0

    # f score: g score + heuristic estimate to goal
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic[start]

    # priority queue stores (f_score, node)
    open_set = [(f_score[start], start)]

    came_from = {}   # for path reconstruction

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return list(reversed(path))
```

#### Example Graph

```python
# Weighted graph
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "D": 2, "E": 5},
    "C": {"A": 4, "F": 3},
    "D": {"B": 2},
    "E": {"B": 5, "H": 2},
    "F": {"C": 3, "G": 2},
    "G": {"F": 2},
    "H": {"E": 2}
}

# Heuristic: estimated distance to goal (G)
heuristic = {
    "A": 7, "B": 6, "C": 5, "D": 4,
    "E": 3, "F": 3, "G": 1, "H": 2
}

path = a_star(graph, "A", "G", heuristic)
print("Path from A to G:", path)
```

**Output:**
```
Path from A to G: ['A', 'C', 'F', 'G']
```

#### How It Works

1. **Initialize:** Set g(start) = 0, f(start) = h(start)
2. **Loop:** While open_set not empty
3. **Pop:** Get node with lowest f-score
4. **Goal Check:** If current is goal, reconstruct path
5. **Expand:** For each neighbor, calculate tentative g-score
6. **Update:** If better path found, update scores and add to queue
7. **Repeat:** Until goal found or open_set empty

**Why A\* Works:**
- **Admissible Heuristic:** h(n) ≤ actual cost to goal
- **Optimal:** Guaranteed shortest path with admissible h(n)
- **Efficient:** Heuristic guides search toward goal

---

### Task 2: Hill Climbing Optimization

**Objective:** Implement hill climbing to find local maxima/minima through iterative improvement.

#### Algorithm Overview

Hill climbing is a greedy local search algorithm that continuously moves toward better neighboring solutions.

**Characteristics:**
- **Greedy:** Always picks best neighbor
- **Local Search:** May get stuck in local optima
- **Fast:** Simple and efficient for good initial states

#### Implementation

```python
import random

# Objective function to maximize
def objective_function(x):
    # Simple mathematical function: -(x - 3)² + 10
    return -(x - 3) ** 2 + 10

# Generate neighbors by small adjustments
def get_neighbors(x):
    step = 0.1
    return [x + step, x - step]

def hill_climbing(start):
    current = start
    current_value = objective_function(current)

    while True:
        neighbors = get_neighbors(current)

        # evaluate neighbors
        best_neighbor = None
        best_value = current_value

        for n in neighbors:
            value = objective_function(n)
            if value > best_value:
                best_value = value
                best_neighbor = n

        # if no neighbor improves the result, stop
        if best_neighbor is None:
            return current, current_value

        # move to the better neighbor
        current = best_neighbor
        current_value = best_value
```

#### Example Usage

```python
# Random starting point
start_point = random.uniform(-10, 10)

solution, value = hill_climbing(start_point)
print("Start point:", start_point)
print("Local maximum at x =", solution)
print("Value:", value)
```

**Sample Output:**
```
Start point: -2.347891
Local maximum at x = 3.0
Value: 10.0
```

#### Visualization

```
Objective Function: -(x - 3)² + 10

   Value
    10 |        *  (maximum at x=3)
     9 |      * * *
     8 |    *     *
     7 |   *       *
     6 |  *         *
       |______________|
       0   1  2  3  4  5  x
```

#### Limitations

1. **Local Optima:** Can get stuck at local peaks
2. **Plateaus:** Flat regions with no improvement
3. **Ridges:** Difficult to navigate diagonal improvements

**Solutions:**
- Random restarts
- Simulated annealing
- Genetic algorithms

---

## 🔍 Algorithm Comparison

| Feature | A\* | Hill Climbing |
|---------|-----|---------------|
| **Type** | Informed search | Local optimization |
| **Completeness** | Complete | Not complete |
| **Optimality** | Optimal (with admissible h) | Not optimal (local) |
| **Memory** | High (stores paths) | Low (current state only) |
| **Use Case** | Pathfinding | Function optimization |
| **Heuristic** | Required | Objective function |

---

## 💡 Key Concepts

### A\* Components
- **Open Set:** Nodes to explore (priority queue)
- **Closed Set:** Already explored nodes
- **g(n):** Path cost so far
- **h(n):** Heuristic estimate
- **f(n) = g(n) + h(n):** Total cost estimate

### Hill Climbing Variants
- **Simple Hill Climbing:** Pick first improvement
- **Steepest Ascent:** Pick best among all neighbors
- **Stochastic:** Random selection among improvements
- **Random Restart:** Multiple attempts from different starts

---

## 🎓 Skills Acquired

✅ A\* pathfinding with heuristics  
✅ Priority queue implementation with heapq  
✅ Path reconstruction from parent pointers  
✅ Hill climbing optimization strategy  
✅ Objective function evaluation  
✅ Local vs global optimization understanding  
✅ Algorithm trade-off analysis  

## 🌍 Real-World Applications

### A\* Applications
- **GPS Navigation:** Route planning with traffic heuristics
- **Game AI:** Character pathfinding in 2D/3D worlds
- **Robotics:** Motion planning and obstacle avoidance
- **Network Routing:** Optimal packet routing

### Hill Climbing Applications
- **Machine Learning:** Parameter tuning
- **Scheduling:** Resource allocation optimization
- **Circuit Design:** Component placement
- **Protein Folding:** Molecular structure prediction

---

## 🔗 Related Files

- **Source Code:** [lab05_astar_hillclimbing.py](../lab05_astar_hillclimbing.py)
- **Previous Lab:** [Lab 4: Graph Traversal Algorithms](lab04_bfs_dfs.md)
- **Main README:** [Repository Overview](../README.md)

---

*Author: Mussa Khan | BS-AI (4th Year)*
