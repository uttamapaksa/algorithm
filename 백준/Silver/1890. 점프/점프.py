N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if not dp[i][j] or not arr[i][j]: continue
        for ni, nj in ((i, j+arr[i][j]), (i+arr[i][j], j)):
            if ni < N and nj < N:
                dp[ni][nj] += dp[i][j]

print(dp[N-1][N-1])