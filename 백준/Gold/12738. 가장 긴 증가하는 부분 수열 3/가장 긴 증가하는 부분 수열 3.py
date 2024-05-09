from bisect import bisect_left

N = int(input())
arr = [*map(int, input().split())]
dp = []

for v in arr:
    idx = bisect_left(dp, v)
    if idx == len(dp):
        dp.append(v)
    elif dp[idx] > v:
        dp[idx] = v

print(len(dp))