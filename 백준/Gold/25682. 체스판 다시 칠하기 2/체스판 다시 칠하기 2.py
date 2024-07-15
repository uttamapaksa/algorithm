import sys; input = sys.stdin.readline
N, M, K = map(int, input().split()); T = K*K
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    board = input()
    for j in range(M):
        if ((i+j)&1 and board[j]=='B') or (not (i+j)&1 and board[j]=='W'):
            dp[i+1][j+1] = 1
        dp[i+1][j+1] += dp[i][j+1] + dp[i+1][j] - dp[i][j]

ans = T
for i in range(K, N+1):
    for j in range(K, M+1):
        val = dp[i][j] - dp[i-K][j] - dp[i][j-K] + dp[i-K][j-K]
        ans = min(ans, val, T-val)
print(ans)