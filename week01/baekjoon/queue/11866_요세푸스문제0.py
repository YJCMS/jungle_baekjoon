import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
queue = deque()
result = []

for i in range(n):
    queue.append(i+1)

while queue:
    for i in range(m-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end="")
print(*result, sep=', ',end="")
print(">")
    
# print("<", ", ".join(res), ">", sep="")
