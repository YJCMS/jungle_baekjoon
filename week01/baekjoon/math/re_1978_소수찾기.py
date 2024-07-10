import sys
n = int(input())
list_n = list(map(int, sys.stdin.readline().split()))
result = 0
for num in list_n:
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    if count == 2 :
        result += 1
print(result)