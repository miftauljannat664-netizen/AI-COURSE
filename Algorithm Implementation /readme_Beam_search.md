Beam Search Algorithm

File: Beam_search.py

**Purpose:**
Implements the Beam Search algorithm, which explores the best k nodes at each level based on heuristic values to find a path to the goal efficiently.

**How it works:**
Beam Search is a heuristic search that limits the number of nodes (beam width) expanded at each level.
It selects only the top-k nodes with the lowest heuristic values and discards the rest, balancing speed and accuracy.

**Complexity:**

Time: O(k × d)

Space: O(k × d)
(k = beam width, d = depth)

**Applications:**
Used in Natural Language Processing (NLP), machine translation, speech recognition, and pathfinding problems.
