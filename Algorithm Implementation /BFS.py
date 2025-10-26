#bfs
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

#  User Input Section
graph = {}

num_nodes = int(input("Enter number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node for BFS: ")
print("BFS Traversal:")
bfs(graph, start_node)
