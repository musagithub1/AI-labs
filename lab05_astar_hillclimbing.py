# Lab 5: AI Search Algorithms - A* and Hill Climbing
# Author: Mussa Khan
# Department: BS-AI (4th Semester)
# Subject: Artificial Intelligence
# Instructor: Farhan Zafar Kayani

# ======================================================
# Task 1: A star Algorithm for Pathfinding
# ======================================================

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


# Example graph with weights
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

# Example heuristic: estimated distance to goal
heuristic = {
    "A": 7,
    "B": 6,
    "C": 5,
    "D": 4,
    "E": 3,
    "F": 3,
    "G": 1,
    "H": 2
}

print("Task 1: A star Path")
path = a_star(graph, "A", "G", heuristic)
print("Path from A to G:", path)


# ======================================================
# Task 2: Hill Climbing Algorithm
# ======================================================

import random

# Objective function to maximize
def objective_function(x):
    # Simple mathematical function
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

# Random starting point
start_point = random.uniform(-10, 10)

print("\nTask 2: Hill Climbing")
solution, value = hill_climbing(start_point)
print("Start point:", start_point)
print("Local maximum at x =", solution)
print("Value:", value)


# ======================================================
# Conclusion
# ======================================================
# In this lab I learned how A star finds the best route using cost and heuristic scores
# and how Hill Climbing searches for better solutions by moving step by step.
# This helped me understand how search algorithms work in artificial intelligence.
