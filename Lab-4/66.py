graph = {
    'A': {'B':2, 'C':3, 'D':4},
    'B': {'A':2, 'D':5, 'F':4},
    'C': {'A':3, 'E':7, 'F':1 },
    'D': {'A':4, 'B':5, 'E':1, 'F':4},
    'E': {'D':1, 'C':7},
    'F': {'B':4, 'C':1, 'D':4}
}

# graph ['A'] = ['B','C','D']
# graph ['B'] = ['A','D','F']
# graph ['C'] = ['A','E','F']
# graph ['D'] = ['A','B', 'E' ,'F']
# graph ['E'] = ['D','C']
# graph ['F'] = ['B','C','D']
def dfs(graph, start, end) :
    stack = [(start, [start], 0)]
    while stack:
        (node, path, distance) = stack.pop()

        for neighbor in set(graph[node]) - set(path):
            if neighbor == end:
                yield  path + [neighbor], distance+graph[node][end]
                stack.append((neighbor, path+ [neighbor],distance + graph[node][neighbor]))

def bfs(graph, start, end) :
    queue = [(start, [start], 0)]
    while queue:
        (node, path, distance) = queue.pop()

        for neighbor in set(graph[node]) - set(path):
            if neighbor == end:
                yield path + [neighbor], distance + graph[node][end]
                queue.append((neighbor, path + [neighbor], distance + graph[node][neighbor]))

start_node = 'A'
end_node = 'D'
dfs_paths = list(dfs(graph, start_node, end_node))
bfs_paths = list(bfs(graph, start_node, end_node))

print("DFS shortest path", min(dfs_paths, key=lambda x:x[1]))
print("BFS shortest path", min(bfs_paths, key=lambda x:x[1]))