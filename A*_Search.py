import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]
    visited = set()
    parent = {start: None}

    while pq:
        f, g, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                parent[neighbor] = node
                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    print("Goal not found")


# Weighted graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 5)],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values to goal F
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}

astar(graph, heuristic, 'A', 'F')
