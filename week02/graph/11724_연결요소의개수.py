import sys
sys.setrecursionlimit(10**8)

def dfs(graph, start, visited):
    visited[start] = True
    for now in graph[start]:
        if not visited[now]:
            dfs(graph, now, visited)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)
