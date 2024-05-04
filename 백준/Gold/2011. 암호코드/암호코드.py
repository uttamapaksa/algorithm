def sol():
    if N == 1 or not arr[1]:
        return 0
    if N == 2:
        return 1

    dp = [0] * N
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N):
        if not arr[i]:
            if arr[i-1] != 1 and arr[i-1] != 2:  # 10, 20
                return 0
            dp[i] += dp[i-2]
        else:
            dp[i] += dp[i-1]
            if arr[i-1] and arr[i-1]*10 + arr[i] <= 26:  # 10 ~ 26
                dp[i] += dp[i-2]
        dp[i] %= 1000000

    return dp[N-1]


arr = [0] + [*map(int, [*input()])]
N = len(arr)
print(sol())