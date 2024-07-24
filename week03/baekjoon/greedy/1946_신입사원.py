import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    vol = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    vol_rank = sorted(vol)
    first = 0
    count = 1
    
    for i in range(1, n):
        if vol_rank[i][1] < vol_rank[first][1]:
            first = i
            count += 1
    
    print(count)
    