import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)  
                  
print(max(dp))

# dp[i] = max(dp[i], dp[j]+1)으로 조건에 맞는 이전 값을 찾았다면,
# 현재 dp[3]에서 가지고 있는 값과 dp[0]+1, dp[1]+1, dp[2]+1을 
# 순서대로 비교하여 결과적으로 가장 긴 과정을 거친 10>20>30인 dp[1]+1이 dp[3]에 들어가서 3이 됩니다.