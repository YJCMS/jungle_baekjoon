import sys

def tsp(n, dist):
    dp = [[None] * n for _ in range(1 << n)]

    def find_cost(mask, i):
        if mask == (1 << n) - 1:
            return dist[i][0] if dist[i][0] > 0 else sys.maxsize
        
        if dp[mask][i] is not None:
            return dp[mask][i]
        
        min_cost = sys.maxsize
        for j in range(n):
            if (mask & (1 << j)) == 0 and dist[i][j] > 0:
                cost = find_cost(mask | (1 << j), j) + dist[i][j]
                min_cost = min(min_cost, cost)

        dp[mask][i] = min_cost
        return dp[mask][i]
    
    return find_cost(1, 0)

n = int(input())
dist = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = tsp(n, dist)
print(result)