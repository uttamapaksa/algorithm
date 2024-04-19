from bisect import bisect_left

# input
N = int(input())
arr = sorted(tuple(map(int, input().split())) for _ in range(N))  # idx, val
vals = [v for _, v in arr]  # val
prev = list(range(N))  # prevIdx
dpi = [-1]
dpv = [-1]

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

# find LIS
idx = dpi[-1]
LIS = set()
while idx != -1:
    LIS.add(vals[idx])
    idx = prev[idx]

# output
answer = f"{N - len(LIS)}"
for i, v in arr:
    if v not in LIS:
        answer += f"\n{i}"
print(answer)