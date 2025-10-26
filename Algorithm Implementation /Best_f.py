#BEST F
import heapq

# Step 1: Build the graph
graph = {}
heuristic = {}

n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    neighbors = input(f"Neighbors of {node} (space separated): ").split()
    graph[node] = neighbors
    h = int(input(f"Heuristic value for {node}: "))
    heuristic[node] = h

# Step 2: Best First Search function
def best_first_search(start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current in visited:
            continue

        print(current, end=" ")
        visited.add(current)

        if current == goal:
            print("\nGoal reached!")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    print("\nGoal not reachable.")

# Step 3: Run the search
start = input("Start node: ")
goal = input("Goal node: ")
best_first_search(start, goal)
