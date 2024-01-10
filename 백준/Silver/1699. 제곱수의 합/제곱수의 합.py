N = int(input())
INF = N+1
dp = [0] + [INF] * N
nums = [i**2 for i in range(1, int(N**0.5) + 1)]

for num in nums:
    for i in range(num, N+1):
        dp[i] = min(dp[i], dp[i-num]+1)

print(dp[N])