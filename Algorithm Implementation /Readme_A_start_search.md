A (A-Star) Search Algorithm*

File: a star search.py

**Purpose:**
Implements the A* search algorithm to find the shortest path from a start node to a goal node using both path cost (g) and heuristic (h).

**How it works:**
A* uses the formula f(n) = g(n) + h(n), where

g(n) = actual cost from start to current node

h(n) = estimated cost from current node to goal
It expands nodes with the smallest f-value first to find the optimal path efficiently.

**Complexity:**

Time: O(E) (worst-case exponential)

Space: O(V)

**Applications:**
Used in GPS navigation, pathfinding in games, robotics, and network routing.




