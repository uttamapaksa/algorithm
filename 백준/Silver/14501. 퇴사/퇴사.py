n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
dp = [[0] * n for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(n-1):
        dp[i][j] = max(dp[i-1][j+1], dp[i-1][j])
    if arr[i-1][0] > n: continue #index 
    dp[i][arr[i-1][0]-1] = max(dp[i-1][0]+arr[i-1][1], dp[i][arr[i-1][0]-1])

print(dp[n][0])