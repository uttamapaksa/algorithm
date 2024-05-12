from bisect import bisect_left

N = int(input())
dp = []

for _ in range(N):
    v = int(input())
    idx = bisect_left(dp, v)
    if idx == len(dp):
        dp.append(v)
    elif dp[idx] > v:
        dp[idx] = v

print(N - len(dp))