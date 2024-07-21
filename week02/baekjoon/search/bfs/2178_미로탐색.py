import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

queue = deque([(0, 0)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))

print(graph[n-1][m-1])