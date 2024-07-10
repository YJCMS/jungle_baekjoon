import sys

def binary_search(x, arr):
    start = 0
    end = n-1 
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            start = mid + 1
        else :
            end = mid - 1
    return False

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in b :
    if binary_search(i, a): 
        print(1)
    else:
        print(0)

