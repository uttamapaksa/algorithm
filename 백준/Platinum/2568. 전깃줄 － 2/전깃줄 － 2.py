from bisect import bisect_left

# static
idxs = []
vals = []
dpi = [-1]
dpv = [-1]

# input
N = int(input())
arr = sorted(tuple(map(int, input().split())) for _ in range(N))  # idx, val
for i, v in arr:
    idxs.append(i)
    vals.append(v)
prev = list(range(N))  # prevIdx

# dp
for idx in range(N):
    val = vals[idx]
    minIdx = bisect_left(dpv, val)
    if minIdx == len(dpv):
        dpv.append(val)
        dpi.append(idx)
        prev[idx] = dpi[minIdx - 1]
    elif val < dpv[minIdx]:
        dpv[minIdx] = val
        dpi[minIdx] = idx
        prev[idx] = dpi[minIdx - 1]

# find non LIS
nonLIS = set(idxs)
idx = dpi[-1]
while idx != -1:
    nonLIS.remove(idxs[idx])
    idx = prev[idx]

# output
answer = f"{len(nonLIS)}\n" + "\n".join(tuple(map(str, sorted(nonLIS))))
print(answer)