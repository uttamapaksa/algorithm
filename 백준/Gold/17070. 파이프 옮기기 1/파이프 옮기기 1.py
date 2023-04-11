N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

if not arr[0][2]:
    dp[0][2] = [1, 0, 0]
    for j in range(3, N):
        if not arr[0][j]: dp[0][j] = [1, 0, 0]
        else: break
    if not arr[1][1] and not arr[1][2]:
        dp[1][2] = [0, 0, 1]
        for i in range(2, N):
            if not arr[i][2]: dp[i][2] = [0, 1, 0]
            else: break

for i in range(1, N):
    for j in range(3, N):
        if not arr[i][j]:
            a, b, c = dp[i][j-1]
            d, e, f = dp[i-1][j]
            dp[i][j][0] += a + c
            dp[i][j][1] += e + f
            if not arr[i-1][j-1] and not arr[i][j-1] and not arr[i-1][j]:
                dp[i][j][2] += sum(dp[i-1][j-1])

print(sum(dp[N-1][N-1]))