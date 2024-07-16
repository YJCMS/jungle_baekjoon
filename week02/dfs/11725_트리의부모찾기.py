import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(node):
    for next_node in graph[node]:
        if visited[next_node] == 0:
            visited[next_node] = node
            dfs(next_node)

dfs(1)

for i in range(2, n+1):
    print(visited[i])