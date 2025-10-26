# DLS (py)
def dls(graph, current, target, limit, visited=None):
    if visited is None:
        visited = set()

    print(f"Visiting {current} at depth limit {limit}")
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

# ----------- User Input Section -------------
graph = {}

num_nodes = int(input("Enter number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node: ")
target_node = input("Enter target node: ")
depth_limit = int(input("Enter depth limit: "))

print("\nDepth Limited Search Traversal:")
found = dls(graph, start_node, target_node, depth_limit)

if not found:
    print(f"\nTarget {target_node} not found within depth limit {depth_limit}")
