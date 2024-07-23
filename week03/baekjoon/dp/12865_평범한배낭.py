import sys

n, k = map(int, sys.stdin.readline().split())
weights = []
values = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    weights.append(a)
    values.append(b)
    
def knapsack(values, weights,capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else: 
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

print(knapsack(values, weights, k))
