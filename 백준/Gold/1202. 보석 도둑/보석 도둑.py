from heapq import heappush, heappop

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
jewels.sort(reverse=True)
bags = [int(input()) for _ in range(K)]
bags.sort()

ans = 0
heap = []
for bag in bags:
    while jewels:
        if jewels[-1][0] <= bag:
            _, V = jewels.pop()
            heappush(heap, -V)
        else:
            break
    if heap:
        ans += -heappop(heap)

print(ans)