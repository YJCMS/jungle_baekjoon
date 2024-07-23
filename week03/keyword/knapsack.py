def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# 예시 데이터
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# 함수 호출
max_value = knapsack(values, weights, capacity)
print(f"배낭에 담을 수 있는 최대 가치: {max_value}")