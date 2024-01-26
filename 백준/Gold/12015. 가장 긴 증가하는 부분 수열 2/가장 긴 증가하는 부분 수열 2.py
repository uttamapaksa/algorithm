from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * (N)
dpmin = [0, 1e8]
dpminkey = {1: 1e8}

for i in range(N):
    min_idx = bisect_left(dpmin, arr[i])
    if min_idx not in dpminkey: # max
        dpmin.append(arr[i])
        dpminkey[min_idx] = arr[i]
    elif dpmin[min_idx] > arr[i]: # bigger
        dpmin[min_idx] = arr[i]
        dpminkey[min_idx] = arr[i]
    dp[i] = min_idx

print(max(dp))