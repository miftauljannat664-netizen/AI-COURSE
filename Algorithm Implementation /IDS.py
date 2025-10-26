def dls(graph, current, target, limit, visited):
    if current == target:
        print(f"Reached target: {target}")
        return True

    if limit <= 0:
        return False

    visited.add(current)
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            if dls(graph, neighbor, target, limit - 1, visited):
                return True

    return False


def ids(graph, start, target, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nTrying depth limit: {depth}")
        visited = set()
        if dls(graph, start, target, depth, visited):
            print("Target found using IDS.")
            return True
    print("Target not found within depth limit.")
    return False

# ----------- User Input Section -------------
graph = {}

num_nodes = int(input("Enter number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node: ")
target_node = input("Enter target node: ")
max_depth = int(input("Enter maximum depth limit: "))

# Run IDS
ids(graph, start_node, target_node, max_depth)
