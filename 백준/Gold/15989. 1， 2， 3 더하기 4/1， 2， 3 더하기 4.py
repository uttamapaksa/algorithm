n = int(input())
arr = [int(input()) for _ in range(n)]
mxv = max(arr)

dp = [1, 1, 2, 3, 4]
for i in range(5, mxv+1):
    dp.append(dp[i-3] + dp[i-2] - dp[i-5] + 1)

for i in arr:
    print(dp[i])