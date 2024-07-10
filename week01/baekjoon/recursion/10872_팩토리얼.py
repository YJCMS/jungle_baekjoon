#재귀함수로 푸는경우
import sys
def factorial(n):
    if n == 0 : return 1
    return n * factorial(n-1)
a = int(sys.stdin.readline())
print(factorial(a))

#반복문으로 푸는경우
# import sys
# n = int(sys.stdin.readline())
# result = n
# if n > 0:
#     for i in range(n-1, 0, -1):
#         result *= i
# else : result = 1
# print(result)   