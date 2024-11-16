from heapq import heappop, heappush

arr = [[] for _ in range(10001)]
for _ in range(int(input())):
    p, d = map(int, input().split())
    arr[d].append(-p)

ans = 0
heap = []
for d in range(10000, 0, -1):
    for p in arr[d]:
        heappush(heap, p)
    if heap:
        ans -= heappop(heap)

print(ans)