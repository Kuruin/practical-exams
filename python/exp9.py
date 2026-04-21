graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [], 'E': [], 'F': []
}

h = {'A': 6, 'B': 4, 'C': 5, 'D': 0, 'E': 0, 'F': 0}

visited = []
queue = [('A', 0)]

while queue:
    queue.sort(key=lambda x: x[1])
    node, cost = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for n, w in graph[node]:
            queue.append((n, w + h[n]))
