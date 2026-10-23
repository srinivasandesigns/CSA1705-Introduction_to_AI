def minimax(tree, node, maximizing):
    # If leaf node, return its value
    if isinstance(tree[node], int):
        return tree[node]

    if maximizing:
        best = float('-inf')
        for child in tree[node]:
            value = minimax(tree, child, False)
            best = max(best, value)
        return best

    else:
        best = float('inf')
        for child in tree[node]:
            value = minimax(tree, child, True)
            best = min(best, value)
        return best


# Game tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}

result = minimax(tree, 'A', True)
print("Minimax value:", result)
