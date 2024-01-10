N = int(input())
cost = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for cnt in range(1, N+1):
    price = cost[cnt]
    for i in range(cnt, N+1):
        dp[i] = max(dp[i], dp[i-cnt] + price)

print(dp[N])