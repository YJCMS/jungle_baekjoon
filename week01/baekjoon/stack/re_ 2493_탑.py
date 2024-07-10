import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * n

for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            result[i] = stack[-1][0] + 1
            break
        else :
            stack.pop()
    stack.append((i, towers[i]))
    
print(*result)


# 실패한 코드
# import sys

# n = int(sys.stdin.readline())
# towers = []
# stack =[]
# result = []
# list = list(map(int, sys.stdin.readline().split(" ")))

# for i in range(n):
#     towers.append([i + 1, list[i]])

# for i in range(len(towers)):
#     tower = towers[1]
#     while stack:
#         prev = tower[1]
#         if prev < tower[1]:
#             stack.pop()
#         if prev > tower[1]:
#             result.append(prev[0])
    
#     if not stack:
#         result.append(0)

#     stack.append(towers[i])

# for i in result:
#     print(i, end=" ")
    