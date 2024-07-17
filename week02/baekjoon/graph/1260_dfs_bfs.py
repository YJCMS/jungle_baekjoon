from collections import defaultdict, deque
import sys

def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    
    return visited

def bfs(graph, start):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    
    return visited

input = sys.stdin.readline
N, M, V = map(int, input().split())
    
graph = [[] for _ in range(N + 1)]
    
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_result = dfs(graph, V)
bfs_result = bfs(graph, V)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
