from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
dp = [1]
dpmin = [0, 1e8]
L = 2 # length of dpmin

for num in arr:
    min_idx = bisect_left(dpmin, num)
    if L == min_idx: # max. index error
        dpmin.append(num)
        L += 1
    elif dpmin[min_idx] > num: # bigger
        dpmin[min_idx] = num
    dp.append(min_idx)

print(max(dp))