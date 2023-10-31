from collections import defaultdict


def dfs(graph, start, end, visited=[], path=[]):
    visited.append(start)
    path.append(start)

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, end, visited, path)
            if new_path:
                return new_path

    path.pop()


def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex == end:
            return path

        for neighbor in graph[vertex]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return None


# Пример использования

# Создаем граф
graph = defaultdict(list)
graph['A'] = ['B', 'C']
graph['B'] = ['E', 'D']
graph['C'] = ['E']
graph['D'] = ['F']
graph['E'] = ['G']
graph['G'] = ['F']
graph['F'] = []
print(graph)
# Используем DFS
dfs_path = dfs(graph, 'A', 'F')
print("DFS Path:", dfs_path)

# Используем BFS
bfs_path = bfs(graph, 'A', 'F')
print("BFS Path:", bfs_path)