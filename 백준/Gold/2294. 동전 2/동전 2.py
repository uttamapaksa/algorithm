N, M = map(int, input().split())
dp = [float('inf')] * (M+1)

coins = []
for _ in range(N):
    coin = int(input())
    if coin <= M:
        coins.append(coin)
        dp[coin] = 1

for i in range(1, M+1):
    for coin in coins:
        if i - coin < 1 or dp[i-coin] == float('inf') : continue
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[i] == float('inf'):
    print(-1)
else:
    print(dp[M])