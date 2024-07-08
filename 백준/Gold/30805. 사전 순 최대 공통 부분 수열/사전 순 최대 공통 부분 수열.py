N = int(input())
arr = [0] + [*map(int, input().split())]
M = int(input())
arr2 = [0] + [*map(int, input().split())]

dp = [[[] for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i] == arr2[j]:
            k = 0
            while k < len(dp[i-1][j-1]):
                if arr2[j] > dp[i-1][j-1][k]:
                    break
                k += 1
            dp[i][j] = [*max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1][:k] + [arr2[j]])]
        else:
            dp[i][j] = [*max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])]

print(len(dp[N][M]))
if len(dp[N][M]): print(*dp[N][M])