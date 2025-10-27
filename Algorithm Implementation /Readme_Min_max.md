Minimax Search Algorithm

File: minimax.py

**Purpose:**
Implements the Minimax algorithm, which is used in game theory and AI to make optimal decisions by minimizing the possible loss in a worst-case scenario.

**How it works:**
The algorithm recursively explores the game tree:

Maximizer chooses the maximum value at even depths.

Minimizer chooses the minimum value at odd depths.
It returns the best value and the path taken from the root to the optimal leaf.

**Complexity:**

Time: O(b^d)

Space: O(d)
(b = branching factor, d = depth of the tree)

**Applications:**
Used in two-player games like Tic-Tac-Toe, Chess, and Checkers for decision-making and strategy planning.
