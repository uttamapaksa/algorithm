N, M, K = map(int, input().split()); T = K*K
dp = [[0] * (M+1)] + [[0] + [*input()] for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if ((i+j) & 1 and dp[i][j] == 'B') or (not ((i+j) & 1) and dp[i][j] == 'W'): dp[i][j] = 1
        else: dp[i][j] = 0
        dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

ans = T
for i in range(K, N+1):
    for j in range(K, M+1):
        val = dp[i][j] - dp[i-K][j] - dp[i][j-K] + dp[i-K][j-K]
        ans = min(ans, val, T-val)
print(ans)