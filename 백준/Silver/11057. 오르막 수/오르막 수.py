N = int(input())
dp = [[0] * 10 for _ in range(N)]
dp[0] = [i for i in range(10, 0, -1)]

for i in range(1, N):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 10007

print(dp[N-1][0])