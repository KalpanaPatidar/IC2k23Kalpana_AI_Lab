from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return order


def dfs(graph, start):
    visited = set()
    order = []

    def explore(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                explore(neighbor)

    explore(start)
    return order


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

print("Graph:", graph)
print("BFS from A:", bfs(graph, 'A'))
print("DFS from A:", dfs(graph, 'A'))
