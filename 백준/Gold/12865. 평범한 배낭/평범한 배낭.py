N, K = map(int, input().split())
knapsack = [[*map(int, input().split())] for _ in range(N)]
dp = [0] * (K+1)

for w, v in knapsack:
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])