graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 4)],
    'D': [], 'E': [], 'F': []
}

visited = []
queue = [('A', 0)]

while queue:
    queue.sort(key=lambda x: x[1])  # sort by cost
    node, cost = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for n, w in graph[node]:
            queue.append((n, w))
