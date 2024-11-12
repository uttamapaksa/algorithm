import sys; input=sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
arr = [[] for _ in range(1001)]
for _ in range(N):
    d, w = map(int, input().split())
    arr[d].append(-w)

ans = 0
heap = []
for day in range(1000, 0, -1):
    for w in arr[day]:
        heappush(heap, w)
    if heap:
        ans -= heappop(heap)

print(ans)