import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split(" ")))
result = []
visited = [0] * n
for i in range(n):
    cost = 0
    for j in (i+1, n):
        if visited[j] == 1:
            pass
        cost += w[i[j]]
        visited[j] = 1
        break
print[result]

