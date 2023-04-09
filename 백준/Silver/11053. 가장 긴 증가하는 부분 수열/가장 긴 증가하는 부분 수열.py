import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
arr = [*map(int, input().split())]
dp = [-1]

for i in range(1, N):
    v = arr[i]
    heap = [0]
    for j in range(i):
        if arr[j] < v:
            heappush(heap, dp[j])
    dp.append(heappop(heap) - 1)

print(-min(dp))