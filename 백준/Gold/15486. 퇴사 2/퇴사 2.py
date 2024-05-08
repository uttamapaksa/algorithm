N = int(input())
dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = max(dp[i], dp[i+1])
    d, w = map(int, input().split())
    if i+d > N:
        continue
    dp[i+d] = max(dp[i+d], dp[i]+w)

print(dp[N])