ans = []

tc = int(input())
for _ in range(tc):
    N = int(input())
    coins = [*map(int, input().split())]
    K = int(input())

    dp = [0] * (K+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, K+1):
            dp[i] += dp[i-coin]

    ans.append(str(dp[K]))

print("\n".join(ans))