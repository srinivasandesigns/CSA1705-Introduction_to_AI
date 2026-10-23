import heapq

def gbfs(graph, heuristic, start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = heapq.heappop(pq)

        if node == goal:
            print("Goal reached:", node)
            return

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        pq, (heuristic[neighbor], neighbor)
                    )

    print("Goal not found")


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic values (estimated distance to goal F)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 0
}

gbfs(graph, heuristic, 'A', 'F')
