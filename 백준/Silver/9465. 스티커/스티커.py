for _ in range(int(input())):
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(2)]
    dp = {0: [arr[0][0], arr[1][0], 0]}
    for i in range(1, n):
        dp[i] = [max(dp[i-1][1], dp[i-1][2]) + arr[0][i], max(dp[i-1][0], dp[i-1][2]) + arr[1][i], max(dp[i-1][0], dp[i-1][1])]
    print(max(dp[n-1]))