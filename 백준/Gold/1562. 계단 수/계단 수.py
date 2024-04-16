N = int(input())
dp = [[[0] * 1024 for _ in range(N)] for _ in range(10)]

for i in range(1, 10):
    dp[i][0][1 << i] = 1
for k in range(1, N):
    for visit in range(1024):
        dp[0][k][visit | (1 << 0)] += dp[1][k-1][visit]
        dp[0][k][visit | (1 << 0)] %= 1000000000
    for i in range(1, 9):
        for visit in range(1024):
            dp[i][k][visit | (1 << i)] += dp[i-1][k-1][visit] + dp[i+1][k-1][visit]
            dp[i][k][visit | (1 << i)] %= 1000000000
    for visit in range(1024):
        dp[9][k][visit | (1 << 9)] += dp[8][k-1][visit]
        dp[9][k][visit | (1 << 9)] %= 1000000000

answer = 0
for i in range(10):
    answer += dp[i][N-1][1023]

print(answer % 1000000000)