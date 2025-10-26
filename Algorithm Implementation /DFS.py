# DFS (Python)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

#  User Input Section
graph = {}

num_nodes = int(input("Enter number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node for DFS: ")
print("DFS Traversal:")
dfs(graph, start_node)
