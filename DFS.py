def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    if start not in visited:
        print(start, end=" ")
        visited.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start DFS from node 'A'
print("DFS Traversal:")
dfs(graph, 'A')
