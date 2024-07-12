import sys

def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited

graph = {
    1: [2,3,4],
    2: [5,6],
    3: [],
    4: [7,8],
    5: [],
    6: [],
    7: [],
    8: [], 
    9: []
}

print(dfs(graph, 1))