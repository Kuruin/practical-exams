graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}


def dls(node, depth):
    if depth == 0:
        return

    print(node, end=" ")

    for i in graph[node]:
        dls(i, depth - 1)


dls('A', 2)
