Alpha-Beta Pruning Algorithm

File: alpha_beta.py

Purpose:
Implements the Minimax algorithm with Alpha-Beta Pruning to optimize game tree search by eliminating unnecessary branches.

How it works:
Alpha-Beta Pruning improves Minimax by skipping nodes that won’t affect the final decision.

Alpha: best value that the maximizer can guarantee.

Beta: best value that the minimizer can guarantee.
Branches are pruned when β ≤ α.

Complexity:

Time: O(b^(d/2)) (with good ordering)

Space: O(d)
(b = branching factor, d = depth of tree)

Applications:
Used in AI-based games like Tic-Tac-Toe, Chess, and Checkers to choose the best move efficiently.
