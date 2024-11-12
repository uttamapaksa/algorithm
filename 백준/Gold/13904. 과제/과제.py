from heapq import heappop, heappush

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

ans = 0
heap = []
for day in range(N, 0, -1):
    while arr and arr[-1][0] >= day:
        heappush(heap, -arr.pop()[1])
    if heap:
        ans -= heappop(heap)

print(ans)