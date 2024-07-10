import sys
import heapq

max_heap = []

n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if max_heap:
            x = heapq.heappop(max_heap)
            print(x[1])
        else: print(0)
    else :
        heapq.heappush(max_heap, (-a, a))

