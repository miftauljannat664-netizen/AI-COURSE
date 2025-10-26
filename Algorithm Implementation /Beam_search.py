# Beam search

# Step 1: Build the graph and heuristic
graph = {}
heuristic = {}

n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node} (space separated): ").split()
    h = int(input(f"Heuristic value for {node}: "))
    heuristic[node] = h

# Step 2: Beam Search with path tracking
def beam_search_with_path(start, goal, beam_width):
    queue = [(start, [start])]  # (current_node, path)
    visited = set()

    while queue:
        print("Current Beam:", " - ".join([node for node, _ in queue]))
        next_level = []

        for node, path in queue:
            visited.add(node)
            if node == goal:
                print(f"\nGoal '{goal}' reached!")
                print("Path:", " → ".join(path))
                return
            for neighbor in graph[node]:
                if neighbor not in visited and all(neighbor != n for n, _ in next_level):
                    next_level.append((neighbor, path + [neighbor]))

        # Sort next level by heuristic and keep top-k (beam width)
        next_level.sort(key=lambda x: heuristic.get(x[0], float('inf')))
        queue = next_level[:beam_width]

    print("\nGoal not reachable.")

# Step 3: Run the search
start = input("Start node: ")
goal = input("Goal node: ")
beam_width = int(input("Beam width (k): "))
beam_search_with_path(start, goal, beam_width)
