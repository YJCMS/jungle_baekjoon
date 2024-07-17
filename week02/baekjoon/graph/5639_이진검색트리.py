import sys
sys.setrecursionlimit(10**8)

arr = []
while True:
    try:
        x = int(sys.stdin.readline())
        arr.append(x)
    except:
        break

def solution(a):
    if len(a) == 0:
        return
    
    left, right = [], []
    mid = a[0]

    for i in range(1, len(a)):
        if a[i] > mid:
            left = a[1:i]
            right = a[i:]
            break

    else:
        left = a[1:]

    solution(left)
    solution(right)
    print(mid)

solution(arr)