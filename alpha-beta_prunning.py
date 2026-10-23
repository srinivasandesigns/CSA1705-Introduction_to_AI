def alphabeta(tree, node, alpha, beta, maximizing):
    # Leaf node
    if isinstance(tree[node], int):
        return tree[node]

    if maximizing:
        value = float('-inf')

        for child in tree[node]:
            value = max(
                value,
                alphabeta(tree, child, alpha, beta, False)
            )
            alpha = max(alpha, value)

            if alpha >= beta:
                break  # Pruning

        return value

    else:
        value = float('inf')

        for child in tree[node]:
            value = min(
                value,
                alphabeta(tree, child, alpha, beta, True)
            )
            beta = min(beta, value)

            if alpha >= beta:
                break  # Pruning

        return value


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

result = alphabeta(
    tree, 'A',
    float('-inf'),
    float('inf'),
    True
)

print("Optimal value:", result)
