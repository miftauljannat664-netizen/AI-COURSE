#Alpha Bita Algorithm

# Step 1: Build the game tree (graph with utilities at leaves)
tree = {}        # adjacency list for game tree
utilities = {}   # leaf node utility values (list)

n = int(input("Number of nodes in the game tree: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    children = input(f"Children of {node} (space separated, leave empty if leaf): ").split()
    if children:
        tree[node] = children
    else:
        vals = list(map(int, input(f"Utility values of leaf node {node} (space separated): ").split()))
        utilities[node] = vals

# Step 2: Minimax with Alpha-Beta Pruning
pruned_nodes = []   # to track pruned branches
prune_count = 0     # total pruning count

def alphabeta(node, depth, alpha, beta, path):
    global prune_count, pruned_nodes

    # Leaf node
    if node in utilities:
        if depth % 2 == 0:   # Maximizer turn
            chosen = max(utilities[node])
        else:                # Minimizer turn
            chosen = min(utilities[node])
        return chosen, path + [f"{node}({chosen})"]

    # Maximizer's turn (even depth)
    if depth % 2 == 0:
        best_val = -999999
        best_path = []
        for child in tree.get(node, []):
            val, new_path = alphabeta(child, depth + 1, alpha, beta, path + [node])
            if val > best_val:
                best_val = val
                best_path = new_path
            alpha = max(alpha, best_val)
            if beta <= alpha:   # Pruning happens
                prune_count += 1
                pruned_nodes.extend(tree[node][tree[node].index(child)+1:])
                break
        return best_val, best_path

    # Minimizer's turn (odd depth)
    else:
        best_val = 999999
        best_path = []
        for child in tree.get(node, []):
            val, new_path = alphabeta(child, depth + 1, alpha, beta, path + [node])
            if val < best_val:
                best_val = val
                best_path = new_path
            beta = min(beta, best_val)
            if beta <= alpha:   # Pruning happens
                prune_count += 1
                pruned_nodes.extend(tree[node][tree[node].index(child)+1:])
                break
        return best_val, best_path

# Step 3: Run the algorithm
root = input("Enter root node of the game tree: ")
value, decision_path = alphabeta(root, 0, -999999, 999999, [])
print(f"\nOptimal value at root '{root}': {value}")
print("Decision path:", " → ".join(decision_path))
print("\nTotal prunings:", prune_count)
print("Pruned nodes:", ", ".join(pruned_nodes) if pruned_nodes else "None")
