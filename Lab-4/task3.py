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

# # Создаем граф
graph = defaultdict(list)
# graph['A'] = ['B', 'C']
# graph['B'] = ['D', 'E']
# graph['C'] = ['E']
# graph['D'] = ['F']
# graph['E'] = ['F']
# graph['F'] = []

graph ['A'] = ['B','C','D']
graph ['B'] = ['A','D','F']
graph ['C'] = ['A','E','F']
graph ['D'] = ['A','B', 'E' ,'F']
graph ['E'] = ['D','C']
graph ['F'] = ['B','C','D']
# graph = {
#     'A': {'B':2, 'C':3, 'D':4},
#     'B': {'A':2, 'D':5, 'F':4},
#     'C': {'A':3, 'E':7, 'F':1 },
#     'D': {'A':4, 'B':5, 'E':1, 'F':4},
#     'E': {'D':1, 'C':7},
#     'F': {'B':4, 'C':1, 'D':4}
# }

# Используем DFS
dfs_path = dfs(graph, 'A', 'D')
print("DFS Path:", dfs_path)

# Используем BFS
bfs_path = bfs(graph, 'A', 'F')
print("BFS Path:", bfs_path)