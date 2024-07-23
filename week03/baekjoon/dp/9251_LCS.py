import sys

x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()

def LCS(x, y):
    m = len(x)
    n = len(y)
    
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]

print(LCS(x, y))