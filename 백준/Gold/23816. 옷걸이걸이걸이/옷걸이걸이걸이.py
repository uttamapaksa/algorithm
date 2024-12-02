n, m = map(int, input().split())
if n >= m:
    print(m)
else:
    dp = [[-1] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    if m >= 3: dp[1][3] = 2
    if m >= 7: dp[1][7] = 4
    if m >= 15:  dp[1][15] = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = j
    for i in range(2, n+1):
        for j in range(i+1, m+1):
            for w, v in ((3,2),(7,4),(15,0)):
                if j >= w and dp[i-1][j-w] != -1 and dp[i][j] < dp[i-1][j-w] + v:
                    dp[i][j] = dp[i-1][j-w] + v
    print(dp[n][m])