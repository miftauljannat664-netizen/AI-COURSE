IDS (Iterative Deepening Search) Algorithm

File: IDS.py

**Purpose:**
Implements Iterative Deepening Search (IDS), which combines the space efficiency of DFS and the completeness of BFS by repeatedly applying Depth-Limited Search with increasing depth.

**How it works:**
Runs DLS multiple times, starting from depth 0 and increasing the limit until the target is found or the maximum depth is reached.

**Complexity:**

Time: O(b^d)

Space: O(d)
(b = branching factor, d = depth of the goal)

**Applications:**
Used in game trees, pathfinding problems, and AI search where the depth of the goal is unknown.
