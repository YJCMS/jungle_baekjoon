import sys
from collections import deque
n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
    rl = sys.stdin.readline().split()
    if rl[0] == 'push' :
        queue.append(rl[1])
    elif rl[0] == 'pop' :
        if not queue: print(-1)
        else: print(queue.popleft())
    elif rl[0] == 'size' :
        print(len(queue))
    elif rl[0] == 'empty' :
        if not queue: print(1)
        else : print(0)
    elif rl[0] == 'front' :
        if not queue: print(-1)
        else: print(queue[0])
    elif rl[0] == 'back' :
        if not queue: print(-1)
        else: print(queue[-1])