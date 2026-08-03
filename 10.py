import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while priority_queue:
        f, cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_cost = cost + weight
                new_f = new_cost + heuristic[neighbor]
                heapq.heappush(
                    priority_queue,
                    (new_f, new_cost, neighbor, path + [neighbor])
                )

    return None, float('inf')

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, cost = astar(start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")