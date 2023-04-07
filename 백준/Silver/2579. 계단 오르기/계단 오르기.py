import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
if N > 1:
    dp = {0: (arr[0], 0), 1: (arr[0] + arr[1], arr[1])}
    for i in range(2, N):
        dp[i] = (dp[i - 1][1] + arr[i], max(dp[i - 2]) + arr[i])
    print(max(dp[N - 1]))
else:
    print(arr[0])
