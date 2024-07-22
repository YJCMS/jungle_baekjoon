import sys

n = sys.stdin.readline().strip().split('-')
arr = []

for i in n:
    sum = 0
    a = i.split('+')
    for j in a:
        sum += int(j)
    arr.append(sum)
    
result = arr[0]

for i in range(1, len(arr)):
    result -= arr[i]
    
print(result)