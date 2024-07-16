import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []

def dfs(graph, start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

dfs(graph, 1)

for i in range(2, n+1):
    print(visited[i])