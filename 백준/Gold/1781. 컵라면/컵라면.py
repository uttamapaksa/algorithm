from heapq import heappop, heappush

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N):
    d, c = map(int, input().split())
    arr[d].append(-c)

ans = 0
heap = []
for d in range(N, 0, -1):
    for p in arr[d]:
        heappush(heap, p)
    if heap:
        ans -= heappop(heap)

print(ans)