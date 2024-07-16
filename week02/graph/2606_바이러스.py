import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(start):
    global count
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            count += 1
            dfs(i)

dfs(1)

print(count)
