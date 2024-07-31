from bisect import bisect_left
_, dp = input(), []
for v in [*map(int, input().split())][::-1]:
    i = bisect_left(dp, v)
    if i == len(dp): dp.append(v)
    elif v < dp[i]: dp[i] = v
print(len(dp))