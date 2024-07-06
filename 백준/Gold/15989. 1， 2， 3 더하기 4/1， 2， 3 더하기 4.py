arr = [int(input()) for _ in range(int(input()))]
mxv = max(arr)

dp = [1, 1, 2, 3, 4]
for i in range(5, mxv+1):
    dp.append(dp[i-3] + dp[i-2] - dp[i-5] + 1)

print('\n'.join(str(dp[i]) for i in arr))