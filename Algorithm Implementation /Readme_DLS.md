DLS (Depth-Limited Search) Algorithm

File: DLS.py

**Purpose:**
Implements Depth-Limited Search, a variation of DFS that explores nodes only up to a given depth limit.

**How it works:**
Starts from the start node, visits nodes recursively up to the specified depth limit, and stops when the target is found or the limit is reached.

**Complexity:**

Time: O(b^l)

Space: O(l)
(b = branching factor, l = depth limit)

**Applications:**
Used in problems where the search depth is known, such as game trees, puzzle solving, and limited-depth graph searches.
