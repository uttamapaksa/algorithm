n, k = map(int, input().split())
coin = {int(input()) for _ in range(n)}
INF = k+1
dp = [0] + [INF] * k

for c in coin:
    for j in range(c, k+1):
        dp[j] = min(dp[j], dp[j-c]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])