N, K = map(int, input().split())
dp = [1] * (K)

for _ in range(N):
    for j in range(1, K):
        dp[j] += dp[j-1]

print(dp[K-1] % 1000000000)