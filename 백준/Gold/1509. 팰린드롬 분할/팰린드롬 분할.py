strs = [*input()]
N = len(strs)
dp = [[3000] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if strs[i] == strs[i+1]:
        dp[i][i+1] = 1

for j in range(2, N):
    for i in range(N):
        if i+j < N and strs[i] == strs[i+j] and dp[i+1][i+j-1] == 1:
            dp[i][i+j] = 1

for i in range(1, N):
    prev = dp[i-1][i-1]
    for j in range(i, N):
        dp[i][j] = min(prev + dp[i][j], dp[i-1][j])

print(dp[N-1][N-1])